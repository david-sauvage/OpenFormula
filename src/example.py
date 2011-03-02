from lpod.document import odf_new_document
from lpod.table import odf_create_table, odf_create_cell

from random import randrange

#import openformula
from syntax import Formula, reference, range_address, column, row
from stats import AVERAGE, MIN, MAX

#We create a spreadsheet just for the example
doc = odf_new_document('spreadsheet')
body = doc.get_body()
table = odf_create_table(u"Data", width=5, height=5)
body.append(table)
for c in range(5):
    for l in range(5):
        v = randrange(0,1000)
        table.set_value((c, l), v)

#Then, we write some statistics about the data in a new sheet
table = odf_create_table(u'Stats', width=3, height=2)
body.append(table)
table.set_value((0,0), u"Average")
table.set_value((1,0), u"Maximum")
table.set_value((2,0), u"Minimum")

#average
formula=Formula(AVERAGE(reference(range_address('data', column('A'), row(1), column('E'), row(5)))))
table.set_cell((0,1), odf_create_cell(formula=formula))

#maximum
formula=Formula(MAX(reference(range_address('data', column('A'), row(1), column('E'), row(5)))))
table.set_cell((1,1), odf_create_cell(formula=formula))

#minimum
formula=Formula(MIN(reference(range_address('data', column('A'), row(1), column('E'), row(5)))))
table.set_cell((2,1), odf_create_cell(formula=formula))

doc.save("out.ods")
