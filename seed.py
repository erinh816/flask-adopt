"""Seed file to make sample data for pets db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
# An alternative if you don't want to drop
# and recreate your tables:
# Pet.query.delete()

# Add pets
woofly = Pet(name='Woofly', species="dog", photo_url="", age="baby",
notes="good dog", available=True)
porchetta = Pet(name='Porchetta', species="porcupine",
photo_url="https://i5.walmartimages.com/seo/Aurora-Medium-Black-Miyoni-10-Porcupine-Adorable-Stuffed-Animal_daa288a5-a706-42a3-828f-831e71802456.1108efc1d57876d093360fd467bdba1f.jpeg?odnHeight=2000&odnWidth=2000&odnBg=FFFFFF",
age="senior",
notes="watch out", available=False)


# Add new objects to session, so they'll persist
db.session.add(woofly)
db.session.add(porchetta)


# Commit--otherwise, this never gets saved!
db.session.commit()
