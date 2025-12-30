from jinja2 import Template

def generate_html_report(df, template_path, output_path):
    with open(template_path) as f:
        template = Template(f.read())

    html = template.render(
        rows=df.to_dict(orient="records"),
        columns=df.columns
    )

    with open(output_path, "w") as f:
        f.write(html)
