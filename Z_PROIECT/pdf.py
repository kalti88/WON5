from xhtml2pdf import pisa
import jinja2
from datetime import date
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "templates/PDF_template.html"
template = templateEnv.get_template(TEMPLATE_FILE)

ord_data = [('22', 'description', '100',), ('22', 'description', '100',), ('22', 'description', '100',), ('22', 'description', '100',), ('22', 'description', '100',)]
supp_data = [('supplier', "address", 'email', 'phone',)]
ord_id = '10'
notes = 'nekrjnverjvnerhvnejhrv'
body = {
    "data": {
        "order_id": ord_id,
        "order": ord_data,
        "supplier": supp_data,
        "note": notes,
        "today": date.today(),
    }
}


outputFilename = "invoice.pdf"


def convertHtmlToPdf(body, outputFilename):
    sourceHtml = template.render(json_data=body["data"])
    resultFile = open(outputFilename, "w+b")
    pisaStatus = pisa.CreatePDF(
            src=sourceHtml,
            dest=resultFile)

    resultFile.close()

    print(pisaStatus.err, type(pisaStatus.err))
    return pisaStatus.err


if __name__ == "__main__":
    pisa.showLogging()
    convertHtmlToPdf(body, outputFilename)
