# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './fusebmc_ui/DlgYaml.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DlgYaml(object):
    def setupUi(self, DlgYaml):
        DlgYaml.setObjectName("DlgYaml")
        DlgYaml.setWindowModality(QtCore.Qt.WindowModal)
        DlgYaml.resize(792, 290)
        DlgYaml.setModal(True)
        self.formLayout = QtWidgets.QFormLayout(DlgYaml)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(DlgYaml)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txtYamlFile = QtWidgets.QLineEdit(DlgYaml)
        self.txtYamlFile.setEnabled(True)
        self.txtYamlFile.setReadOnly(True)
        self.txtYamlFile.setObjectName("txtYamlFile")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtYamlFile)
        self.label_2 = QtWidgets.QLabel(DlgYaml)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txtInput_file = QtWidgets.QLineEdit(DlgYaml)
        self.txtInput_file.setEnabled(True)
        self.txtInput_file.setReadOnly(True)
        self.txtInput_file.setObjectName("txtInput_file")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtInput_file)
        self.label_3 = QtWidgets.QLabel(DlgYaml)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txtLanguage = QtWidgets.QLineEdit(DlgYaml)
        self.txtLanguage.setEnabled(True)
        self.txtLanguage.setReadOnly(True)
        self.txtLanguage.setObjectName("txtLanguage")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.txtLanguage)
        self.label_4 = QtWidgets.QLabel(DlgYaml)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(DlgYaml)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.txtData_model = QtWidgets.QLineEdit(DlgYaml)
        self.txtData_model.setEnabled(True)
        self.txtData_model.setReadOnly(True)
        self.txtData_model.setObjectName("txtData_model")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.txtData_model)
        self.buttonBox = QtWidgets.QDialogButtonBox(DlgYaml)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.label_6 = QtWidgets.QLabel(DlgYaml)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.txtArch = QtWidgets.QLineEdit(DlgYaml)
        self.txtArch.setEnabled(True)
        self.txtArch.setReadOnly(True)
        self.txtArch.setObjectName("txtArch")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.txtArch)
        self.cmbProperties = QtWidgets.QComboBox(DlgYaml)
        self.cmbProperties.setObjectName("cmbProperties")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cmbProperties)

        self.retranslateUi(DlgYaml)
        self.buttonBox.accepted.connect(DlgYaml.accept) # type: ignore
        self.buttonBox.rejected.connect(DlgYaml.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DlgYaml)

    def retranslateUi(self, DlgYaml):
        _translate = QtCore.QCoreApplication.translate
        DlgYaml.setWindowTitle(_translate("DlgYaml", "Yaml Parser"))
        self.label.setText(_translate("DlgYaml", "Yaml file"))
        self.label_2.setText(_translate("DlgYaml", "Input_file"))
        self.label_3.setText(_translate("DlgYaml", "Language"))
        self.label_4.setText(_translate("DlgYaml", "Properties"))
        self.label_5.setText(_translate("DlgYaml", "Data_model"))
        self.label_6.setText(_translate("DlgYaml", "Arch"))
