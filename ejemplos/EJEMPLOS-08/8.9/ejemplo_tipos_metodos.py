
class MiFichero:
    path_name="./miaplicacion/"
    def __init__(self, filename):
        self.filename= filename

    '''
    MÉTODOS CRUD
    '''
    def save(self,linea) ->bool:
        try:
            with open(self.path_name+self.filename,"a") as f:
                f.write(linea)
                return True
        except Exception as e:
            return False

    @classmethod
    def set_path_name(cls,path_name):
        cls.path_name = path_name
if __name__ == "__main__":

    mi_fichero_1=MiFichero("miaplicacion1.txt")
    mi_fichero_1.save("Nueva linea")

    mi_fichero_2 = MiFichero("miaplicacion2.txt")
    mi_fichero_2.save("Nueva linea")

    MiFichero.set_path_name("./miaplicacion2/")

    mi_fichero_1 = MiFichero("miaplicacion1.txt")
    mi_fichero_1.save("Nueva linea2")

    mi_fichero_2 = MiFichero("miaplicacion2.txt")
    mi_fichero_2.save("Nueva linea2")