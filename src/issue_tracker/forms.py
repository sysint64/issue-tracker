class Widget:
    def render(self, field):
        raise NotImplemented()

    def fields(self, field):
        yield self


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
    def fields(self, field):
        for i in range(field["extra"]):
            yield self


class Validator:
    def __init__(self):
        self.errors = []

    def is_valid(self, value):
        raise NotImplemented()

    def get_errors(self):
        return self.errors


class RequireValidator(Validator):
    pass


def render_functor(form):
    def _render(request, field):
        widget = field["widget"]()

        if "decorator" in field:
            return field["decorator"].render(widget, field)

        if "form.decorator" in form:
            return form["form.decorator"].render(widget, field)

        return widget.render(field)

    return _render


def fields(form):
    for key in form.keys():
        if key[0:5] == "form.":
            continue

        field = form[key]

        if "id" not in field:
            field["id"] = key

        if "name" not in field:
            field["name"] = key

        if "label" not in field:
            field["label"] = key.capitalize()

        if "value" not in field:
            field["value"] = ""

        field["render"] = render_functor(form)
        yield field


class FieldDecorator:
    def render(self, widget, field):
        raise NotImplemented()


class DivFieldDecorator(FieldDecorator):
    def __init__(self, css_class=""):
        self.css_class = css_class

    def render(self, widget, field):
        return f'<div class="{self.css_class}">{widget.render(field)}</div>'
