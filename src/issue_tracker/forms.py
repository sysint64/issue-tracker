class Widget:
    def __init__(self, form, field):
        self.field = field
        self.form = form

    def render(self, field):
        raise NotImplemented()


class TextWidget(Widget):
    def render(self, field):
        return f"""
            <label for="{field["id"]}">{field["label"]}</label>
            <input type="text" id="{field["id"]}" name="{field["name"]}" value="{field["value"]}">
        """


class TextAreaWidget(Widget):
    def render(self, field):
        return f"""
            <label for="{field["id"]}">{field["label"]}</label>
            <textarea type="text" id="{field["id"]}" name="{field["name"]}">{field["value"]}</textarea>
        """


class MultipleFieldsWidget(Widget):
    def __init__(self, form, field):
        super().__init__(form, field)
        count_key = f"{field['name']}.count"
        count = self.form.data[count_key] if count_key in self.form.data.keys() else field["extra"]

        if "form.decorator" in self.form.declaration:
            field["fields"]["form.decorator"] = self.form.declaration["form.decorator"]

        def create_form(idx):
            decl = field["fields"].copy()
            decl["form.field_prefix"] = f"{field['name']}[{idx}]."
            return decl

        field["forms"] = [create_form("x")]
        field["forms"][0]["form.decorator"] = DivFieldDecorator(css_class="hidden")

        for i in range(count):
            field["forms"].append(create_form(str(i)))

    def render(self, field):
        html = ""

        for form_declaration in field["forms"]:
            for child_field in fields(self.form, form_declaration, self.form.data):
                child_field["render"] = render_functor(self.form, form_declaration)
                html += child_field["render"](None, child_field)

        return html


class Validator:
    def __init__(self):
        self.errors = []

    def is_valid(self, value):
        raise NotImplemented()

    def get_errors(self):
        return self.errors


class RequireValidator(Validator):
    pass


class FieldDecorator:
    def render(self, widget, field):
        raise NotImplemented()


class DivFieldDecorator(FieldDecorator):
    def __init__(self, css_class=""):
        self.css_class = css_class

    def render(self, widget, field):
        return f'<div class="{self.css_class}">{widget.render(field)}</div>'


def render_functor(form, declaration):
    def _render(request, field):
        # Create widget instance
        widget = field["widget"](form, field)

        if "decorator" in field:
            return field["decorator"].render(widget, field)

        if "form.decorator" in declaration:
            return declaration["form.decorator"].render(widget, field)

        return widget.render(field)

    return _render


def fields(form, declaration, data=None):
    if data is None:
        data = {}

    if "form.field_prefix" not in declaration:
        declaration["form.field_prefix"] = ""

    prefix = declaration["form.field_prefix"]

    for key in declaration.keys():
        if key[0:5] == "form.":
            continue

        field = declaration[key]

        if "label" not in field:
            field["label"] = key.capitalize()

        field_name = prefix + key
        field["id"] = field_name
        field["name"] = field_name
        initial_value = field["initial_value"] if "initial_value" in field else ""
        field["value"] = data[field_name] if field_name in data.keys() else initial_value
        field["render"] = render_functor(form, declaration)

        yield field


def form_is_valid(form):
    return form["form.is_valid"] if "form.is_valid" in form else True


class Form:
    def __init__(self, declaration, data=None):
        self.declaration = declaration
        self.data = data

    def __iter__(self):
        return fields(self, self.declaration, self.data)

    def is_valid(self):
        return True
