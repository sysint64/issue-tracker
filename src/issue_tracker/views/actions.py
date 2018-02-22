import aiohttp_jinja2


class Widget:
    def render(self, field):
        raise NotImplemented()

    def fields(self, field):
        yield self


class TextWidget(Widget):
    def render(self, field):
        return f"""
            <label>
                <b>{field["label"]}</b><br>
                <input type="text" id={field["id"]} name="{field["name"]}" value="{field["value"]}">
            </label>
        """


class TextAreaWidget(Widget):
    def render(self, field):
        return f"""
            <label>
                <b>{field["label"]}</b><br>
                <textarea type="text" id={field["id"]} name="{field["name"]}">{field["value"]}</textarea>
            </label>
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


class DivDecorator:
    def __init__(self, css_class=""):
        self.css_class = css_class

    def render(self, widget, field):
        return f'<div class="{self.css_class}">{widget.render(field)}</div>'


@aiohttp_jinja2.template("issues_create.html.j2")
def issues_create(request):
    form = {
        "form.decorator": DivDecorator(css_class="form-field"),
        "form.field_prefix": "create_issues.",
        "name": {
            "widget": TextWidget,
            "validators": [RequireValidator]
        },
        "desc": {
            "decorator": DivDecorator(css_class="desc-form-field"),
            "widget": TextAreaWidget,
            "label": "Description",
        },
        # "items": {
        #     "widget": MultipleFieldsWidget,
        #     "label": "Content",
        #     "extras": 1,
        #     "fields": {
        #         "name": {
        #             "field": TextWidget,
        #             "validators": [RequireValidator]
        #         },
        #         "desc": {
        #             "field": TextAreaWidget,
        #             "validators": [RequireValidator]
        #         }
        #     }
        # }
    }

    output = {
        "errors": ["Some error"],
        "name": {
            "errors": ["This field is required"],
            "value": ""
        },
        "desc": {
            "value": "Some interesting desc"
        },
        "items": [
            {
                "name": {
                    "value": "Test"
                },
                "desc": {
                    "value": "Lolipop"
                }
            },
            {
                "name": {
                    "value": "Test"
                },
                "desc": {
                    "value": "Lolipop"
                }
            },
        ]
    }

    return {
        "page_title": "Create issue",
        "form": fields(form),
    }
