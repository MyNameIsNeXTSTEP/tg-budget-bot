import telegram
from telegram import Update
from telegram.ext import ContextTypes
from app.handlers.response import send_response
from app.handlers.keyboards import get_categories_keyboard
from app.services.days import getDaysBaseInfo
from app import config
from app.templates import render_template


async def all_days(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # @Aspect
    # When received from a command like: /days 20
    # commandDaysCount = update.message.text.split()[1] - expected to be (20)
    # For further DB selection of bunch of days, then send a .xslx file using xlsxwriter
    some_days_info = list(await getDaysBaseInfo())
    if not update.message:
        return

    await send_response(
        update,
        context,
        render_template(
            "day.j2",
            {"info": some_days_info[0], "start_index": None},
        ),
        # @Aspect - use inline keyboard interface properly
        # get_categories_keyboard(
        #     current_category_index=0,
        #     categories_count=len(some_days_info),
        #     callback_prefix=config.ALL_DAYS_CALLBACK_PATTERN,
        # ),
    )

# TODO: rethink how to handle TG buttons for DAYs class
async def all_days_button(update: Update, _: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if not query.data or not query.data.strip():
        return
    categories_with_books = list(await getDaysBaseInfo())
    current_category_index = _get_current_category_index(query.data)
    await query.edit_message_text(
        text=render_template(
            "day.j2",
            {
                "category": categories_with_books[current_category_index],
                "start_index": None,
            },
        ),
        # TODO: figure out what is it for and how works (raply_markup)
        # reply_markup=get_categories_keyboard(
        #     current_category_index=current_category_index,
        #     categories_count=len(categories_with_books),
        #     callback_prefix=config.ALL_BOOKS_CALLBACK_PATTERN,
        # ),
        parse_mode=telegram.constants.ParseMode.HTML,
    )


def _get_current_category_index(query_data) -> int:
    pattern_prefix_length = len(config.ALL_BOOKS_CALLBACK_PATTERN) # wrong config element (rudiment)
    return int(query_data[pattern_prefix_length:])
