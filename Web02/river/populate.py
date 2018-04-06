from models.river import River
import mlab

mlab.connect()

river1 = River(
                    name = "Amazone",
                    continent = "S.America",
                    length = 6992
                  )
river1.save()

river2 = River(
                    name = "Congo",
                    continent = "Africa",
                    length = 4371
                  )
river2.save()

river3 = River(
                    name = "Orinoco",
                    continent = "S.America",
                    length = 2140
                  )
river3.save()
