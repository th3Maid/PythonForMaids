from core.maid import MaidChild

maid = MaidChild(
    "cass",
    "cassandra",
    "todos",
    {
        "seg": "lavar pratos",
        "ter": "trocar diferencial l200",
        "qui": "lavar dogge ram"
    }
)

print(maid.schedule())
print(maid.f_schedule())