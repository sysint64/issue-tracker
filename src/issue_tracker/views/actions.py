import aiohttp_jinja2


class Widget:
    def render(self, field):
        raise NotImplemented()

    def fields(self, field):
        yield self


class TextWidget(Widget):
    def render(self, field):
        return f"""
            <div>
            <label>
                <b>{field["label"]}</b><br>
                <input type="text" id={field["id"]} name="{field["name"]}" value="{field["value"]}">
            </label>
            </div>
        """


class TextAreaWidget(Widget):
    def render(self, field):
        return f"""
            <div>
            <label>
                <b>{field["label"]}</b><br>
                <textarea type="text" id={field["id"]} name="{field["name"]}">{field["value"]}</textarea>
            </label>
            </div>
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


def render(request, field):
    return field["widget"]().render(field)


@aiohttp_jinja2.template("issues_create.html.j2")
def issues_create(request):
    form = {
        "name": {
            "value": "",
            "id": "name",
            "name": "name",
            "widget": TextWidget,
            "label": "Name",
            "validators": [RequireValidator],
            "render": render
        },
        "desc": {
            "value": "",
            "id": "desc",
            "name": "desc",
            "widget": TextAreaWidget,
            "label": "Description",
            "render": render
        },
        # "items": {
        #     "field": MultipleFieldsWidget,
        #     "label": "Content",
        #     "extras": 0,
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

    def fields(fields):
        for key in fields.keys():
            field = fields[key]
            yield field

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
