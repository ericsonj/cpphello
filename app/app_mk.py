from pymakelib import module


@module.ModuleClass
class App(module.AbstractModule):
    
    def getSrcs(self) -> list:
        return [
            'app/src/main.cpp'
        ]

    def getIncs(self) -> list:
        return [

        ]