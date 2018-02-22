import aiohttp_jinja2
from issue_tracker.forms import *


@aiohttp_jinja2.template("issues_create.html.j2")
def issues_create(request):
    form = {
        "form.decorator": DivFieldDecorator(css_class="form-field"),
        "form.field_prefix": "create_issues.",
        "name": {
            "widget": TextWidget,
            "validators": [RequireValidator]
        },
        "desc": {
            "decorator": DivFieldDecorator(css_class="desc-form-field"),
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
