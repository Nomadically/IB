from pydbisam import PyDBISAM

# with PyDBISAM("//paradise/P/Channergy2/data/Customer.dat") as db:
with PyDBISAM(r"C:\Users\ib\Documents\YC-Main\backupOf1-Channergy\Channergy\data\Items.dat") as db:
	print(", ".join(db.fields()))
	for row in db.rows():
		print(", ".join(map(str, row)))