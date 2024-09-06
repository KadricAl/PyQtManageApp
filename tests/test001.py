from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport

app = QtWidgets.QApplication([])

w = QtWidgets.QTableWidget(10, 10)
for i in range(10):
    for j in range(10):
        it = QtWidgets.QTableWidgetItem("{}-{}".format(i, j))
        w.setItem(i, j, it)


filename = "table.pdf"
model = w.model()

printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.PrinterResolution)
printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
printer.setPaperSize(QtPrintSupport.QPrinter.A4)
printer.setOrientation(QtPrintSupport.QPrinter.Landscape)
printer.setOutputFileName(filename)

doc = QtGui.QTextDocument()

html = """<html>
<head>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>
</head>"""
html += "<table><thead>"
html += "<tr>"
for c in range(model.columnCount()):
    html += "<th>{}</th>".format(model.headerData(c, QtCore.Qt.Horizontal))

html += "</tr></thead>"
html += "<tbody>"
for r in range(model.rowCount()):
    html += "<tr>"
    for c in range(model.columnCount()):
        html += "<td>{}</td>".format(model.index(r, c).data() or "")
    html += "</tr>"
html += "</tbody></table>"
doc.setHtml(html)
doc.setPageSize(QtCore.QSizeF(printer.pageRect().size()))
doc.print_(printer)