from .user import *
from .admin import *
from aiogram.types import ContentType

# DON'T TOUCH THIS IMPORT
from loader import dp


def setup(dp):
    """setup handlers for users and moders in one place and add throttling in 5 seconds

    Args:
        dp (Dispatcher): Dispatcher object
    """

    """user handlers"""
    dp.register_message_handler(
        cmd_start,
        commands=['start'],
        state=None)

    dp.register_message_handler(
        cmd_pay,
        lambda message: message.text.startswith('💵'),
        state=None)

    dp.register_pre_checkout_query_handler(
        pre_checkout_query_handler, lambda query: True)

    dp.register_message_handler(
        successful_payment_handler, content_types=ContentType.SUCCESSFUL_PAYMENT)

    dp.register_message_handler(
        cmd_my_configs,
        text='📁 Мои конфиги',
        state=None)

    dp.register_message_handler(
        cmd_menu,
        text='🔙 Назад',
        state=None)

    dp.register_callback_query_handler(
        device_selected,
        lambda call: call.data.endswith('config_create_request'),
        state=New_config.device)

    dp.register_callback_query_handler(
        cancel_config_creation,
        lambda call: call.data == 'cancel_config_creation',
        state=New_config.device)

    dp.register_message_handler(
        create_new_config,
        text='🆕 Создать конфиг',
        state=None)

    dp.register_message_handler(
        cmd_show_config,
        lambda message: message.text.startswith('🔐'),
        state=None)

    dp.register_message_handler(
        cmd_support,
        text='📝 Помощь',)

    dp.register_message_handler(
        cmd_show_end_time,
        text='📅 Дата отключения',)

    dp.register_message_handler(
        cmd_show_subscription,
        text='🕑 Моя подписка',)

    """moder handlers"""
    dp.register_message_handler(
        cmd_info,
        commands=["info"],
        state=None)

    dp.register_message_handler(
        statistic_endtime,
        commands=["stats"],
        state=None)

    dp.register_message_handler(
        give_subscription_time,
        commands=["give"],
        state=None)
