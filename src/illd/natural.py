"""
This Blueprint holds displays for displays that are on the natural
support, the one that Dismod-AT uses for its computation.
"""
import logging

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session,
    current_app
)
from illd.db import get_db


LOGGER = logging.getLogger(__name__)
NATURAL_BP = Blueprint("natural", __name__, url_prefix="/natural")


@NATURAL_BP.route("/show/<meid>")
def show(meid):
    """
    Load a visualization that is on the underlying grids.

    Args:
        meid: Uniform Resource Identifier with which to get the data.
    """
    LOGGER.warning(f"meid is {meid}")
    g.meid = meid
    if "URI" not in current_app.config:
        current_app.config["URI"] = "none"
    db = get_db()

    fig = figure(plot_width=300, plot_height=300)
    fig.vbar(x=[1, 2, 3, 4], width=0.5, bottom=0, top=[1.7, 2.2, 4.6, 3.9], color="navy")
    script, div = components(fig)

    return encode_utf8(
        render_template(
            "natural.html",
            uri=current_app.config["URI"],
            plot_script=script,
            plot_div=div,
            js_resources=INLINE.render_js(),
            css_resources=INLINE.render_css(),
        )
    )


@NATURAL_BP.route("/update/<uri>")
def update(uri):
    """
    Assign a new URI to what is being shown.

    Args:
        uri: The one to update.
    """
    updated = request.args.get("uri", "")
    LOGGER.warning(f"Updating uri to {updated}")
    current_app.config["URI"] = updated
    return f"Updating to {updated}\n"
