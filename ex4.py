from __future__ import annotations


class Person:
    def __init__(self, name: str, birthday: str):
        self.name: str = name
        self.birthday: str = birthday
        self.parents: list[Person] = []
        self.partner: Person | None = None
        self.children: list[Person] = []

    def setParents(self, p1: Person, p2: Person) -> None:
        if len(self.parents) >= 2:
            raise ValueError("Person already has two parents")
        self.parents.append(p1)
        self.parents.append(p2)

        p1.children.append(self)
        p2.children.append(self)

    def setPartner(self, p: Person, /) -> None:
        if self.partner or p.partner:
            raise ValueError("Person already has a partner")
        self.partner = p
        p.partner = self

    def tree(self) -> str:
        return (
            f'{self.name} {f"- {self.partner.name}" if self.partner else ""}'
            + "\n\t"
            + "\n\t".join(child.tree() for child in self.children)
        )


if __name__ == '__main__':
    p1 = Person ("James", "1920.10.02")
    p2 = Person ("Jane", "1925.10.02")

    p1.setPartner(p2)

    p3 = Person ("Johny", "1950.09.12")

    p3.setParents(p1, p2)

    p4 = Person ("Jenny", "1950.03.22")

    p4.setParents(p1, p2)

    p5 = Person ("Merry", "1980.01.23")
    p6 = Person ("Terry", "1980.06.22")

    p3.setPartner(p5)
    p4.setPartner(p6)

    p7 = Person ("Selina", "1982.10.02")
    p8 = Person ("Meita", "1950.12.12")
    p9 = Person ("Mark", "1954.12.22")

    p7.setParents(p4, p6)
    p8.setParents(p4, p6)
    p9.setParents(p4, p6)

    p10 = Person ("Django", "1982.10.02")
    p11= Person ("Melina", "1950.12.12")

    p10.setParents(p3, p5)
    p11.setParents(p3, p5)

    print (p1.tree())