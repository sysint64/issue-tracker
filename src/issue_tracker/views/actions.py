import aiohttp_jinja2
from issue_tracker.forms import *


@aiohttp_jinja2.template("issues_create.html.j2")
async def issues_create(request):
    form_declaration = {
        "form.decorator": DivFieldDecorator(css_class="form-field"),
        "form.field_prefix": "create_issues.",
        "name": {
            "widget": TextWidget,
            "validators": [RequireValidator],
        },
        "desc": {
            "decorator": DivFieldDecorator(css_class="desc-form-field"),
            "widget": TextAreaWidget,
            "label": "Description",
        },
        "items": {
            "widget": MultipleFieldsWidget,
            "label": "Content",
            "extra": 2,
            "fields": {
                "name": {
                    "widget": TextWidget,
                    "validators": [RequireValidator]
                },
                "desc": {
                    "widget": TextAreaWidget,
                    "validators": [RequireValidator]
                }
            }
        }
    }

    data = await request.post()
    form = Form(form_declaration, data)

    form.is_valid()

    return {
        "page_title": "Create issue",
        "form": form,
    }
