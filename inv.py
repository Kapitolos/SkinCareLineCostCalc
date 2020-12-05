class Ingredient:
    def __init__(self,name, units, cost):
        self.name = name
        self.units = units
        self.cost = cost

class Product:
    def __init__(self, name, Ingredient, *ratio, cost):
        self.name = name
        self.Ingredient = Ingredient
        self.ratio = ratio
        self.cost = cost

    def pricefind(self, Ingredient, ratio, cost):
        result = Ingredient / ratio
        price = cost / result
        return price

    def totals(self, Ingredient, ratio, cost):
        amount_result = []
        ratio_result = []
        cost_result = []
        for amount in self.Ingredient:
            amount_result += amount
        for ratios in self.ratio:
            ratio_result = ratios
        for costs in self.cost:
            cost_result += costs
        amount_result = sum(amount_result)
        ratio_result = sum(ratio_result)
        cost_result = sum(cost_result)
        Product.total = self.pricefind(amount_result,ratio_result,cost_result)

#The ingredients. Name, size of standard usage in ml, price of that usage.
# ie: Beeswax, 480ml(1 pound), $10 a pound.
beeswax_pnd = Ingredient('Beeswax', [480], [10])
app_oil = Ingredient('Appricot', [4000], [48.28])
broccoli_oil = Ingredient('Broccoli Oil', [473], [84.92])
cane_sugar = Ingredient('Cane Sugar', [1056], [5.75])
frankincense_oil = Ingredient ('Frankincense Oil', [100], [12.36])
green_clay = Ingredient ('Green Clay', [1056], [25.83])
hemp_seed_oil = Ingredient ('Hemp Seed Oil', [1000], [17.96])
jojoba_oil = Ingredient ('Jojoba Oil', [1000], [54.12])
orange_sweet_oil = Ingredient ('Orange Sweet Oil', [100], [5.78])
patchouli_oil =Ingredient ('Pathouli Oil', [100], [16.20])
pomegranate_oil = Ingredient ('Pomegranate Oil', [473], [92.10])
sage_oil = Ingredient ('Sage Oil', [100], [19.50])
elderflower_petals = Ingredient('Elderflower Petals', [480], [37.05])
coconut_oil = Ingredient('Coconut Oil', [2480], [16.99])
grapeseed_oil= Ingredient('Grapeseed Oil', [1000], [8.05])
calendula = Ingredient('Calendula', [227], [13.35])
calendula_infused_app_oil = Ingredient('Calendula Infused Appricot Oil', [4000], [61.63])
rosehip_oil = Ingredient('Rosehip Oil', [1000], [141.24])
cocoa_butter = Ingredient('Cocoa Butter', [528], [16.16])
shea_butter = Ingredient('Shea Butter', [1056], [16.50])
cedarwood_oil = Ingredient('Cedarwood Oil', [500], [28.45])
cypress_oil = Ingredient ('Cypress Oil', [500], [77.90])
grapefruit_oil = Ingredient ('Grapefruit Oil', [100], [26.60])
peppermint_oil = Ingredient ('Peppermint Oil', [100], [14.43])
bergamont_oil= Ingredient('Bergamont Oil', [100], [22.56])
geranium_oil = Ingredient('Geranium Oil' , [100], [27.08])
lavender_oil = Ingredient('Lavender Oil', [500], [92.84])
eucalyptus_oil = Ingredient ('Eucalyptus Oil', [500], [55])
vetiver_oil = Ingredient ('Vetiver Oil', [15], [25.84])
balsam_fir_oil = Ingredient('Balsam Fir Oil', [100], [18.40])
nutmeg_oil = Ingredient('Nutmeg Oil', [15], [8.58])
org_coffee = Ingredient('Coffee', [250], [5] )
raw_brown_sugar = Ingredient('Brown Sugar', [1000], [5.75])
jar100ml = Ingredient('Jar100ml', [1], [1])
jar50ml = Ingredient ("Jar50ml", [1], [.60])
label_100ml = Ingredient('Label 100ml', [48], [24])
label_50ml = Ingredient('Label 50ml', [48], [12])
bottle_blue_glass = Ingredient ('Blue Glass Bottle', [1], [1])
lip_balm_tin15ml = Ingredient('Lip Balm Tin', [1],[.64])
lip_balm_tin_label = Ingredient ('Lip Balm Tin Label', [60], [8])
kraft_tube = Ingredient ('Kraft Tube',[1],[1.18])
kraft_tube_label = Ingredient('Kraft Tube Label', [1], [.36])
castile_soap = Ingredient('Castile Soap', [1000], [16.94])


#Products are here. Name, ingredients.units, ratio of use in ml, cost=ingredient.cost
coconut_body_balm = Product(('Coconut Body Balm'), [beeswax_pnd.units, app_oil.units, coconut_oil.units, jar100ml.units, label_100ml.units], [16.66, 16.66, 66.66, 1., 1.], cost=(beeswax_pnd.cost, app_oil.cost, coconut_oil.cost, jar100ml.cost, label_100ml.cost))
cedarwood_body_balm = Product (('Cedarwood Body Balm'), [beeswax_pnd.units, coconut_oil.units, app_oil.units, cedarwood_oil.units, cypress_oil.units,jar100ml.units, label_100ml.units], [16.66, 16.66, 66.66, 1.25, 1.25, 1, 24], cost = (beeswax_pnd.cost, coconut_oil.cost,app_oil.cost, cedarwood_oil.cost, cypress_oil.cost, jar100ml.cost, label_100ml.cost))
bergamont_geranium_body_balm = Product(('Bergamont Geranium Body Balm'), [beeswax_pnd.units, coconut_oil.units, app_oil.units, cedarwood_oil.units, cypress_oil.units, jar100ml.units, label_100ml.units], [16.66, 66.66, 16.66, 1.8, .7, 1, 24], cost= (beeswax_pnd.cost, coconut_oil.cost, app_oil.cost, cedarwood_oil.cost, cypress_oil.cost, jar100ml.cost, label_100ml.cost))
lavender_eucalyptus_body_balm = Product(('Lavender Eucalyptus Body Balm'), [beeswax_pnd.units, shea_butter.units, app_oil.units, cedarwood_oil.units, cypress_oil.units, jar100ml.units, label_100ml.units],[16.66,16.66,66.66,1.25,1.25, 1, 24], cost= (beeswax_pnd.cost,shea_butter.cost,app_oil.cost,cedarwood_oil.cost,cypress_oil.cost,jar100ml.cost,label_100ml.cost))
tattoo_pop = Product(('Tattoo Pop'),[beeswax_pnd.units,coconut_oil.units,hemp_seed_oil.units,sage_oil.units,patchouli_oil.units,jar100ml.units,label_100ml.units],[16.66,16.66,66.66,.83,.83,1,24], cost =(beeswax_pnd.cost,coconut_oil.cost,hemp_seed_oil.cost,sage_oil.cost,patchouli_oil.cost,jar100ml.cost,label_100ml.cost))
restorative_face_serum = Product(('Restore Face Serum'), [jojoba_oil.units,calendula_infused_app_oil.units,pomegranate_oil.units,rosehip_oil.units,broccoli_oil.units,geranium_oil.units,frankincense_oil.units, bottle_blue_glass.units, label_50ml.units], [18.18,9.09,9.09,9.09,4.54,.31,.41,1,24],cost = (jojoba_oil.cost, calendula_infused_app_oil.cost, pomegranate_oil.cost,rosehip_oil.cost,broccoli_oil.cost,geranium_oil.cost,frankincense_oil.cost,bottle_blue_glass.cost,label_50ml.cost))
healing_face_oil = Product(('Healing Face Oil'), [calendula.units, elderflower_petals.units, app_oil.units, bottle_blue_glass.units, label_50ml.units], [8.33,8.33,33.32, 1, 24], cost = (calendula.cost,elderflower_petals.cost,app_oil.cost,bottle_blue_glass.cost,label_50ml.cost))
coffee_peppermint_scrub = Product(('Coffee Scrub'), [app_oil.units,castile_soap.units,green_clay.units,cane_sugar.units,org_coffee.units,peppermint_oil.units, jar100ml.units, label_100ml.units],[12.5,12.5,25,25,25,.62,1,24],cost = (app_oil.cost,castile_soap.cost,green_clay.cost,cane_sugar.cost,org_coffee.cost,peppermint_oil.cost,jar100ml.cost,label_100ml.cost))
healing_face_salve = Product(('Healing Face Salve'), [beeswax_pnd.units,coconut_oil.units,grapeseed_oil.units,calendula_infused_app_oil.units,rosehip_oil.units, jar50ml.units,label_50ml.units],[8.33,8.33,12.45,16.66,4.16,1,24],cost =(beeswax_pnd.cost,coconut_oil.cost,grapeseed_oil.cost,calendula_infused_app_oil.cost,rosehip_oil.cost,jar50ml.cost,label_50ml.cost))
beard_balm = Product(('Beard Balm'), [beeswax_pnd.units, grapeseed_oil.units, app_oil.units, nutmeg_oil.units, balsam_fir_oil.units, vetiver_oil.units, label_50ml.units, jar50ml.units],[10,20,20,.833,.30,.123,1,24], cost=(beeswax_pnd.cost,grapeseed_oil.cost,app_oil.cost,nutmeg_oil.cost,balsam_fir_oil.cost,vetiver_oil.cost,label_50ml.cost,jar50ml.cost))
cocao_lip_balm_tin = Product(('Cocao Lip Balm TIN'), [beeswax_pnd.units,coconut_oil.units,calendula_infused_app_oil.units,cocoa_butter.units,lip_balm_tin_label.units,lip_balm_tin15ml.units],[3,6,3,3,1,1],cost=(beeswax_pnd.cost,coconut_oil.cost,calendula_infused_app_oil.cost,cocoa_butter.cost,lip_balm_tin_label.cost,lip_balm_tin15ml.cost))
grapefuit_lip_balm_tin = Product(('Grapefruit Lip Balm TIN'), [beeswax_pnd.units,coconut_oil.units,calendula_infused_app_oil.units,shea_butter.units,grapefruit_oil.units,lip_balm_tin_label.units,lip_balm_tin15ml.units],[3,6,3,3,.375,1,1],cost=(beeswax_pnd.cost,coconut_oil.cost,calendula_infused_app_oil.cost,shea_butter.cost,grapefruit_oil.cost,lip_balm_tin_label.cost,lip_balm_tin15ml.cost))
peppermint_lip_balm_tin = Product(('Peppermint Lip Balm TIN'), [beeswax_pnd.units,calendula_infused_app_oil.units,shea_butter.units,peppermint_oil.units,lip_balm_tin_label.units,lip_balm_tin15ml.units],[3,6,6,.375,1,1],cost=(beeswax_pnd.cost,calendula_infused_app_oil.cost,shea_butter.cost,peppermint_oil.cost,lip_balm_tin_label.cost,lip_balm_tin15ml.cost))
cocao_lip_balm_tube = Product(('Cocao Lip Balm TUBE'),[beeswax_pnd.units,coconut_oil.units,calendula_infused_app_oil.units,cocoa_butter.units,kraft_tube_label.units,kraft_tube.units],[1.6,3.2,1.6,1.6,1,1],cost=(beeswax_pnd.cost,coconut_oil.cost,calendula_infused_app_oil.cost,cocoa_butter.cost,kraft_tube_label.cost,kraft_tube.cost))
grapefuit_lip_balm_tube = Product(('Grapefruit Lip Balm TUBE'),[beeswax_pnd.units,coconut_oil.units,calendula_infused_app_oil.units,shea_butter.units,grapefruit_oil.units,kraft_tube_label.units,kraft_tube.units],[1.6,3.2,1.6,1.6,.2,1,1],cost=(beeswax_pnd.cost,coconut_oil.cost,calendula_infused_app_oil.cost,shea_butter.cost,grapefruit_oil.cost,kraft_tube_label.cost,kraft_tube.cost))
peppermint_lip_balm_tube = Product(('Peppermint Lip Balm TUBE'),[beeswax_pnd.units,calendula_infused_app_oil.units,shea_butter.units,peppermint_oil.units,kraft_tube_label.units,kraft_tube.units],[1.6,3.2,3.2,.2,1,1],cost=(beeswax_pnd.cost,calendula_infused_app_oil.cost,shea_butter.cost,peppermint_oil.cost,kraft_tube_label.cost,kraft_tube.cost))

prod = {
    'Bergamont Geranium Body Balm': bergamont_geranium_body_balm,
    'Lavender Eucalyptus Body Balm': lavender_eucalyptus_body_balm,
    'Tattoo Pop': tattoo_pop,
    'Restore Face Serum': restorative_face_serum,
    'Healing Face Oil' : healing_face_oil,
    'Healing Face Salve' : healing_face_salve,
    'Coffee Scrub': coffee_peppermint_scrub,
    'Coconut Body Balm' : coconut_body_balm,
    'Cedarwood Body Balm' : cedarwood_body_balm,
    'Beard Balm' : beard_balm,
    'Cocao Lip Balm TIN' : cocao_lip_balm_tin,
    'Grapefruit Lip Balm TIN': grapefuit_lip_balm_tin,
    'Peppermint Lip Balm TIN' : peppermint_lip_balm_tin ,
    'Cocao Lip Balm TUBE' : cocao_lip_balm_tube ,
    'Grapefruit Lip Balm TUBE' : grapefuit_lip_balm_tube ,
    'Peppermint Lip Balm TUBE' : peppermint_lip_balm_tube
}




