# -*- coding: utf-8 -*-
"""
/***************************************************************************
 tipeData
                                 A QGIS plugin
 Imprime el tipo de la capa
                             -------------------
        begin                : 2016-04-13
        copyright            : (C) 2016 by Cristhian Forero Fernando Pineda / Universidad Distrital Francisco José de Caldas
        email                : wfpinedar@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load tipeData class from file tipeData.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .tipedata import tipeData
    return tipeData(iface)
