from odoo import models, fields
class AgenceVehicule(models.Model):
    _name = 'agence.vehicule'
    _description='App Démo-Agence de Location de Véhicules'
    _order = 'date_achat desc, marque'
    _rec_name = 'designation_vehicule'
    # Les caractéristiques des véhicules
    marque = fields.Char('Marque', required=True)
    modele = fields.Char('Modele', required=True)
    matricule = fields.Char('Matricule', required=True)
    designation_vehicule= fields.Char('Désingation')
    date_achat = fields.Date("Date d Achat")
    chaffeur_ids = fields.Many2many(
        'res.partner',
        string='Chaffeurs'
    )

    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s -%s -%s" % (record.marque, record.modele, record.matricule)
            result.append((record.id, rec_name))
        return result