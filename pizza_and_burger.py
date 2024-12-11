class Pizza:  # product
    def __init__(self):
        self.dough = None
        self.size = None
        self.sauce = None
        self.filling = None

    def __str__(self):
        return (f'Ваша пицца, тесто у нее {self.dough},'
                f' размер {self.size},'
                f' добавлено соус {self.sauce}'
                f' и начинка {self.filling} ')


class Burger:  # product
    def __init__(self):
        self.type_of_bun = None
        self.cutlet = None
        self.supplement = None

    def __str__(self):
        return (f'Ваш бургер, булочка {self.type_of_bun},'
                f'котлета {self.cutlet},'
                f'добавлено {self.supplement}')


class PizzaBuilder:  # builder for pizza
    def __init__(self):
        self.pizza = Pizza()

    def choose_the_dough(self, dough: str):
        self.pizza.dough = dough
        return self

    def choose_the_size(self, size: str):
        self.pizza.size = size
        return self

    def build(self):
        return self.pizza

    def choose_the_sauce(self, sauce: str):
        self.pizza.sauce = sauce
        return self

    def choose_the_filling(self, filling: str):
        self.pizza.filling = filling
        return self


class BurgerBuilder:  # builder for burger
    def __init__(self):
        self.burger = Burger()

    def choose_the_bun(self, bun: str):
        self.burger.type_of_bun = bun
        return self

    def choose_the_cutlet(self, cutlet: str):
        self.burger.cutlet = cutlet
        return self

    def choose_the_additives(self, supplement: str):
        self.burger.supplement = supplement
        return self

    def build(self):
        return self.burger


class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def assemble_pizza(self):
        return (
            self.builder.choose_the_dough('тонкое')
            .choose_the_size('маленькая')
            .choose_the_sauce('томат')
            .choose_the_filling('сыр')
            .build()
        )


class BurgerDirector:
    def __init__(self, builder: BurgerBuilder):
        self.builder = builder

    def assemble_burger(self):
        return (
            self.builder.choose_the_bun('классическая')
            .choose_the_cutlet('курица')
            .choose_the_additives('сыр')
            .build()
        )


p_builder = PizzaBuilder()
p_director = PizzaDirector(p_builder)
pizza = p_director.assemble_pizza()
print(pizza.__str__())


