# -*- coding: utf-8 -*-
# Copyright 2017 Akretion
# @author Raphaël Valyi <raphael.valyi@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'L10n Br Account Payment CNAB Brcobranca',
    'description': """
        Imprime boletos usando a Gem brcobranca do Boletosimples""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Akretion',
    'website': 'www.akretion.com',
    'depends': [
        'l10n_br_account_payment_cobranca',
    ],
    'data': [
        'views/payment_mode.xml',
        'views/l10n_br_cnab_retorno_view.xml',
        'data/cnab_data.xml',
    ],
    'demo': [
    ],
    'test': [
        'tests/invoice_create.yml'
    ]
}
