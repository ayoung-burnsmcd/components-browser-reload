from django_components import component

@component.register("test")
class Test(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found. To customize which template to use based on context
    # you can override def get_template_name() instead of specifying the below variable.
    template_name = "test/test.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(self):
        return {
            "value": "foo",
        }