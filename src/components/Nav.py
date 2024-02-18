from dash import html

layout = html.Nav(
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
                ),
        html.P('esCova - 2024')
    ],
    className='nav-links'
)