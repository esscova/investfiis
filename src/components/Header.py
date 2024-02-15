from dash import Dash, html

layout = html.Header(
    [
        html.H1("Dashboard"),
        html.Nav(
            [
                html.Ul(
                    [
                        html.Li(
                            html.A(
                                html.Img(src="../../assets/img/linkedin-logo.png"),
                                href="https://www.linkedin.com/in/wellington-moreira-santos/",
                                target="_blank",
                            )
                        ),
                        html.Li(
                            html.A(
                                html.Img(src="../../assets/img/github-logo.png"),
                                href="https://github.com/wellington-moreira-santos/Scraping-fiis",
                                target="_blank",
                            )
                        ),
                    ]
                )
            ]
        ),
    ]
)
