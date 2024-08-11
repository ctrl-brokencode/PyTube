# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pytubeXFbVvN.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QCursor, QFont, QIcon, QPixmap
from PySide6.QtWidgets import (QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(895, 592)
        MainWindow.setStyleSheet(u"QMessageBox QLabel {\n"
"	color: #000;\n"
"}\n"
"\n"
"* {\n"
"	border: 0px solid white;\n"
"}\n"
"\n"
"* QLabel {\n"
"	color: #FFF;\n"
"}\n"
"\n"
"QPushButton, QToolButton {\n"
"	border: 0;\n"
"}\n"
"\n"
"#central_widget, #pages_stacked_widget > QWidget {\n"
"	background-color: #110200;\n"
"}\n"
"\n"
"#header, #menu_lateral, #frame_pages {\n"
"	border: 2px solid #fff;\n"
"}\n"
"\n"
"/* Header */\n"
"#input_pesquisa {\n"
"	background-color: transparent;\n"
"	border: 1px solid #FFF;\n"
"	padding: 2px 6px;\n"
"	color: #FFF;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"#menu_lateral QToolButton {\n"
"	fill: #FFF;\n"
"}\n"
"\n"
"/* P\u00e1gina V\u00eddeo */\n"
"#frame_pag_video {\n"
"	background-color: transparent;\n"
"	border: 1px solid #FFF;\n"
"	color: #FFF;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"#frame_video {\n"
"	border: 1px solid #FFF;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"#frame_video_btns QPushButton {\n"
"	color: #FFF;\n"
"	border: 1px solid #FFF;\n"
"	border-radius: 9px;\n"
"	padding: 1px 20px;\n"
"}\n"
"\n"
""
                        "#btn_baixar_audio {\n"
"	background-color: #900000;\n"
"}\n"
"#btn_baixar_audio::hover {\n"
"	background-color: #AF1C1C;\n"
"}\n"
"\n"
"#btn_baixar_video {\n"
"	background-color: #833803;\n"
"}\n"
"#btn_baixar_video::hover {\n"
"	background-color: #AB581E;\n"
"}\n"
"\n"
"#frame_qualidade QComboBox {\n"
"	background-color: #FFBBBB;\n"
"	border: 1px solid #FFF;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/icons/angle-down.svg);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid darkgray;\n"
"	color: #FFF;\n"
"	background-color: #5D1B1B;\n"
"}\n"
"")
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.verticalLayout = QVBoxLayout(self.central_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.central_widget)
        self.header.setObjectName(u"header")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header)
        self.horizontalLayout_4.setSpacing(100)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_header_left = QFrame(self.header)
        self.frame_header_left.setObjectName(u"frame_header_left")
        self.frame_header_left.setFrameShape(QFrame.StyledPanel)
        self.frame_header_left.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_header_left)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 0, 0, 0)
        self.btn_menu = QToolButton(self.frame_header_left)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/menu-burger.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.btn_menu)

        self.frame_logo = QFrame(self.frame_header_left)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setFrameShape(QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_logo)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.logo = QLabel(self.frame_logo)
        self.logo.setObjectName(u"logo")

        self.horizontalLayout_9.addWidget(self.logo)

        self.label = QLabel(self.frame_logo)
        self.label.setObjectName(u"label")

        self.horizontalLayout_9.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.frame_logo)


        self.horizontalLayout_4.addWidget(self.frame_header_left)

        self.frame_pesquisa = QFrame(self.header)
        self.frame_pesquisa.setObjectName(u"frame_pesquisa")
        self.frame_pesquisa.setFrameShape(QFrame.StyledPanel)
        self.frame_pesquisa.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_pesquisa)
        self.horizontalLayout_2.setSpacing(13)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.input_pesquisa = QLineEdit(self.frame_pesquisa)
        self.input_pesquisa.setObjectName(u"input_pesquisa")

        self.horizontalLayout_2.addWidget(self.input_pesquisa)

        self.btn_pesquisar = QToolButton(self.frame_pesquisa)
        self.btn_pesquisar.setObjectName(u"btn_pesquisar")
        self.btn_pesquisar.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pesquisar.setIcon(icon1)
        self.btn_pesquisar.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_pesquisar)


        self.horizontalLayout_4.addWidget(self.frame_pesquisa)

        self.horizontalSpacer = QSpacerItem(282, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.header)

        self.main_frame = QFrame(self.central_widget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_lateral = QFrame(self.main_frame)
        self.menu_lateral.setObjectName(u"menu_lateral")
        self.menu_lateral.setFrameShape(QFrame.StyledPanel)
        self.menu_lateral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.menu_lateral)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menu_btns = QFrame(self.menu_lateral)
        self.menu_btns.setObjectName(u"menu_btns")
        self.menu_btns.setFrameShape(QFrame.StyledPanel)
        self.menu_btns.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.menu_btns)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_pag_home = QToolButton(self.menu_btns)
        self.btn_pag_home.setObjectName(u"btn_pag_home")
        self.btn_pag_home.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pag_home.setIcon(icon2)
        self.btn_pag_home.setIconSize(QSize(24, 24))
        self.btn_pag_home.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.btn_pag_home.setArrowType(Qt.NoArrow)

        self.verticalLayout_5.addWidget(self.btn_pag_home)

        self.btn_pag_video = QToolButton(self.menu_btns)
        self.btn_pag_video.setObjectName(u"btn_pag_video")
        self.btn_pag_video.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/play-alt-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pag_video.setIcon(icon3)
        self.btn_pag_video.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btn_pag_video)

        self.btn_pag_pasta = QToolButton(self.menu_btns)
        self.btn_pag_pasta.setObjectName(u"btn_pag_pasta")
        self.btn_pag_pasta.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/folder-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pag_pasta.setIcon(icon4)
        self.btn_pag_pasta.setIconSize(QSize(24, 24))
        self.btn_pag_pasta.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.verticalLayout_5.addWidget(self.btn_pag_pasta)


        self.verticalLayout_2.addWidget(self.menu_btns, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.menu_lateral)

        self.frame_pages = QFrame(self.main_frame)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_pages)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.paginas = QStackedWidget(self.frame_pages)
        self.paginas.setObjectName(u"paginas")
        self.pag_home = QWidget()
        self.pag_home.setObjectName(u"pag_home")
        self.verticalLayout_3 = QVBoxLayout(self.pag_home)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_centro_home = QFrame(self.pag_home)
        self.frame_centro_home.setObjectName(u"frame_centro_home")
        self.frame_centro_home.setFrameShape(QFrame.StyledPanel)
        self.frame_centro_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_centro_home)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.topo_centro = QFrame(self.frame_centro_home)
        self.topo_centro.setObjectName(u"topo_centro")
        self.topo_centro.setFrameShape(QFrame.StyledPanel)
        self.topo_centro.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.topo_centro)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.logo_2 = QLabel(self.topo_centro)
        self.logo_2.setObjectName(u"logo_2")
        self.logo_2.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout_6.addWidget(self.logo_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_4.addWidget(self.topo_centro)

        self.meio_centro = QFrame(self.frame_centro_home)
        self.meio_centro.setObjectName(u"meio_centro")
        self.meio_centro.setFrameShape(QFrame.StyledPanel)
        self.meio_centro.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.meio_centro)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_logo = QLabel(self.meio_centro)
        self.label_logo.setObjectName(u"label_logo")

        self.horizontalLayout_7.addWidget(self.label_logo, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_4.addWidget(self.meio_centro)

        self.baixo_centro = QFrame(self.frame_centro_home)
        self.baixo_centro.setObjectName(u"baixo_centro")
        self.baixo_centro.setFrameShape(QFrame.StyledPanel)
        self.baixo_centro.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.baixo_centro)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_descricao = QLabel(self.baixo_centro)
        self.label_descricao.setObjectName(u"label_descricao")

        self.horizontalLayout_8.addWidget(self.label_descricao, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_4.addWidget(self.baixo_centro)


        self.verticalLayout_3.addWidget(self.frame_centro_home, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.paginas.addWidget(self.pag_home)
        self.pag_video = QWidget()
        self.pag_video.setObjectName(u"pag_video")
        self.verticalLayout_8 = QVBoxLayout(self.pag_video)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_pag_video = QFrame(self.pag_video)
        self.frame_pag_video.setObjectName(u"frame_pag_video")
        self.frame_pag_video.setFrameShape(QFrame.StyledPanel)
        self.frame_pag_video.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_pag_video)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame__info_video = QFrame(self.frame_pag_video)
        self.frame__info_video.setObjectName(u"frame__info_video")
        self.frame__info_video.setFrameShape(QFrame.StyledPanel)
        self.frame__info_video.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame__info_video)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_video = QFrame(self.frame__info_video)
        self.frame_video.setObjectName(u"frame_video")
        self.frame_video.setFrameShape(QFrame.StyledPanel)
        self.frame_video.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_video)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.icone_video = QLabel(self.frame_video)
        self.icone_video.setObjectName(u"icone_video")
        self.icone_video.setMaximumSize(QSize(32, 32))
        self.icone_video.setPixmap(QPixmap(u":/icons/play.svg"))
        self.icone_video.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.icone_video)

        self.nome_video = QLabel(self.frame_video)
        self.nome_video.setObjectName(u"nome_video")
        font = QFont()
        font.setFamilies([u"Ebrima"])
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.nome_video.setFont(font)
        self.nome_video.setWordWrap(True)

        self.horizontalLayout_11.addWidget(self.nome_video)


        self.verticalLayout_6.addWidget(self.frame_video)

        self.label_nome_autor = QLabel(self.frame__info_video)
        self.label_nome_autor.setObjectName(u"label_nome_autor")
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(13)
        font1.setItalic(True)
        self.label_nome_autor.setFont(font1)
        self.label_nome_autor.setMargin(0)

        self.verticalLayout_6.addWidget(self.label_nome_autor)

        self.frame_dura_view = QFrame(self.frame__info_video)
        self.frame_dura_view.setObjectName(u"frame_dura_view")
        self.frame_dura_view.setFrameShape(QFrame.StyledPanel)
        self.frame_dura_view.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_dura_view)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_duracao = QFrame(self.frame_dura_view)
        self.frame_duracao.setObjectName(u"frame_duracao")
        self.frame_duracao.setFrameShape(QFrame.StyledPanel)
        self.frame_duracao.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_duracao)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_duracao = QLabel(self.frame_duracao)
        self.label_duracao.setObjectName(u"label_duracao")
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(11)
        self.label_duracao.setFont(font2)

        self.horizontalLayout_12.addWidget(self.label_duracao)


        self.horizontalLayout_13.addWidget(self.frame_duracao)

        self.frame_views = QFrame(self.frame_dura_view)
        self.frame_views.setObjectName(u"frame_views")
        self.frame_views.setFrameShape(QFrame.StyledPanel)
        self.frame_views.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_views)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_views = QLabel(self.frame_views)
        self.label_views.setObjectName(u"label_views")
        self.label_views.setFont(font2)

        self.horizontalLayout_14.addWidget(self.label_views)


        self.horizontalLayout_13.addWidget(self.frame_views)


        self.verticalLayout_6.addWidget(self.frame_dura_view)


        self.verticalLayout_7.addWidget(self.frame__info_video)

        self.frame_qualidade = QFrame(self.frame_pag_video)
        self.frame_qualidade.setObjectName(u"frame_qualidade")
        font3 = QFont()
        font3.setPointSize(8)
        self.frame_qualidade.setFont(font3)
        self.frame_qualidade.setFrameShape(QFrame.StyledPanel)
        self.frame_qualidade.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_qualidade)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(25)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setContentsMargins(10, 0, 10, 10)
        self.qualidade_audio = QComboBox(self.frame_qualidade)
        self.qualidade_audio.setObjectName(u"qualidade_audio")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.qualidade_audio.setFont(font4)
        self.qualidade_audio.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.qualidade_audio, 1, 0, 1, 1)

        self.qualidade_video = QComboBox(self.frame_qualidade)
        self.qualidade_video.setObjectName(u"qualidade_video")
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setItalic(False)
        self.qualidade_video.setFont(font5)
        self.qualidade_video.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.qualidade_video, 1, 1, 1, 1)

        self.label_qualidade_audio = QLabel(self.frame_qualidade)
        self.label_qualidade_audio.setObjectName(u"label_qualidade_audio")
        font6 = QFont()
        font6.setFamilies([u"Comic Sans MS"])
        font6.setPointSize(11)
        font6.setBold(False)
        font6.setItalic(True)
        self.label_qualidade_audio.setFont(font6)

        self.gridLayout.addWidget(self.label_qualidade_audio, 0, 0, 1, 1, Qt.AlignHCenter)

        self.label_qualidade_video = QLabel(self.frame_qualidade)
        self.label_qualidade_video.setObjectName(u"label_qualidade_video")
        self.label_qualidade_video.setFont(font6)

        self.gridLayout.addWidget(self.label_qualidade_video, 0, 1, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.frame_qualidade)

        self.frame_video_btns = QFrame(self.frame_pag_video)
        self.frame_video_btns.setObjectName(u"frame_video_btns")
        self.frame_video_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_video_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_video_btns)
        self.horizontalLayout_10.setSpacing(25)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(10, 0, 10, 0)
        self.btn_baixar_audio = QPushButton(self.frame_video_btns)
        self.btn_baixar_audio.setObjectName(u"btn_baixar_audio")
        font7 = QFont()
        font7.setFamilies([u"Microsoft YaHei"])
        font7.setPointSize(12)
        font7.setBold(True)
        self.btn_baixar_audio.setFont(font7)
        self.btn_baixar_audio.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.btn_baixar_audio)

        self.btn_baixar_video = QPushButton(self.frame_video_btns)
        self.btn_baixar_video.setObjectName(u"btn_baixar_video")
        self.btn_baixar_video.setFont(font7)
        self.btn_baixar_video.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.btn_baixar_video)


        self.verticalLayout_7.addWidget(self.frame_video_btns)


        self.verticalLayout_8.addWidget(self.frame_pag_video, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.paginas.addWidget(self.pag_video)
        self.pag_carregando = QWidget()
        self.pag_carregando.setObjectName(u"pag_carregando")
        self.horizontalLayout_15 = QHBoxLayout(self.pag_carregando)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_pag_carregando = QFrame(self.pag_carregando)
        self.frame_pag_carregando.setObjectName(u"frame_pag_carregando")
        self.frame_pag_carregando.setFrameShape(QFrame.StyledPanel)
        self.frame_pag_carregando.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_pag_carregando)
        self.verticalLayout_9.setSpacing(20)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_carregando = QLabel(self.frame_pag_carregando)
        self.label_carregando.setObjectName(u"label_carregando")
        font8 = QFont()
        font8.setFamilies([u"Ebrima"])
        font8.setPointSize(19)
        font8.setBold(True)
        self.label_carregando.setFont(font8)

        self.verticalLayout_9.addWidget(self.label_carregando)

        self.progresso = QProgressBar(self.frame_pag_carregando)
        self.progresso.setObjectName(u"progresso")
        font9 = QFont()
        font9.setFamilies([u"Calibri Light"])
        font9.setBold(True)
        font9.setItalic(True)
        self.progresso.setFont(font9)
        self.progresso.setValue(90)
        self.progresso.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.progresso)


        self.horizontalLayout_15.addWidget(self.frame_pag_carregando, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.paginas.addWidget(self.pag_carregando)

        self.horizontalLayout_5.addWidget(self.paginas)


        self.horizontalLayout.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)

        self.paginas.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icon-32x32.png\"/></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Logo", None))
        self.input_pesquisa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisa ou URL", None))
        self.btn_pesquisar.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_pag_video.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.logo_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icon-200x200.png\"/></p></body></html>", None))
        self.label_logo.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo brabo", None))
        self.label_descricao.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o mais top que j\u00e1 existiu", None))
        self.nome_video.setText(QCoreApplication.translate("MainWindow", u"Nome do V\u00eddeo", None))
        self.label_nome_autor.setText(QCoreApplication.translate("MainWindow", u"Por: Nome do Autor", None))
        self.label_duracao.setText(QCoreApplication.translate("MainWindow", u"Dura\u00e7\u00e3o: 0:00", None))
        self.label_views.setText(QCoreApplication.translate("MainWindow", u"Views: 0", None))
        self.label_qualidade_audio.setText(QCoreApplication.translate("MainWindow", u"Qualidade \u00c1udio", None))
        self.label_qualidade_video.setText(QCoreApplication.translate("MainWindow", u"Qualidade V\u00eddeo", None))
        self.btn_baixar_audio.setText(QCoreApplication.translate("MainWindow", u"Baixar \u00c1udio", None))
        self.btn_baixar_video.setText(QCoreApplication.translate("MainWindow", u"Baixar V\u00eddeo", None))
        self.label_carregando.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Carregando...</p></body></html>", None))
    # retranslateUi

