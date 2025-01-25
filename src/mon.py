from src.attack import Attack

class Mon:
    def __init__(self, hp: int, sp: int, atk: int, df: int, satk: int, sdf: int, spd: int, main_type: str, sub_type: str, attacks:list[any]=[]):
        self.hp = hp
        self.sp = sp
        self.atk = atk
        self.df = df
        self.satk = satk
        self.sdf = sdf
        self.spd = spd
        self.main_type = main_type
        self.sub_type = sub_type
        self.attacks = attacks

    @property
    def hp(self) -> int:
        return self.__hp

    @hp.setter
    def hp(self, hp: int) -> int:
        self.check_for_valid_stat(hp)
        self.__hp = hp

    @property
    def sp(self) -> int:
        return self.__sp

    @sp.setter
    def sp(self, sp) -> int:
        self.check_for_valid_stat(sp)
        self.__sp = sp

    @property
    def atk(self) -> int:
        return self.__atk
    
        
    @atk.setter
    def atk(self, atk) -> int:
        self.check_for_valid_stat(atk)
        self.__atk = atk

    @property
    def df(self) -> int:
        return self.__df

    
    @df.setter
    def df(self, df) -> int:
        self.check_for_valid_stat(df)
        self.__df = df
    
    @property
    def satk(self) -> int:
        return self.__satk

    @satk.setter
    def satk(self, satk) -> int:
        self.check_for_valid_stat(satk)
        self.__satk = satk
    
    @property
    def sdf(self) -> int:
        return self.__sdf
    
    @sdf.setter
    def sdf(self, sdf) -> int:
        self.check_for_valid_stat(sdf)
        self.__sdf = sdf
    
    @property
    def spd(self) -> int:
        return self.__spd
    
    @spd.setter
    def spd(self, spd) -> int:
        self.check_for_valid_stat(spd)
        self.__spd = spd

    @property
    def main_type(self) -> str:
        return self.__main_type
    
    @property
    def sub_type(self) -> str:
        return self.__sub_type
    
    @property
    def attacks(self) -> list[any]:
        return list(self.__attacks)

    @property
    def main_type(self) -> str:
        return self.__main_type
    
    @property
    def sub_type(self) -> str:
        return self.__sub_type
    
    @property
    def attacks(self) -> list[any]:
        return list(self.__attacks)

    def check_for_valid_stat(self, stat): 
        if not isinstance(stat, int):
            raise TypeError(f"{stat} must be an integer")
        if not 0 < stat <= 255:
            raise TypeError(f"{stat} must be between 1 and 255")
        
    def check_for_valid_attack(self, attack): 
        if not isinstance(attack, Attack):
            raise TypeError(f"{attack.name} must be an Attack obj")
