from dash import Dash, html
from src.components import Header, SectionCards,SectionGraphs

layout = html.Main([
    Header.layout,
    SectionCards.layout,
    SectionGraphs.layout,
])