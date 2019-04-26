from operator import itemgetter

GOAL = 500.0


class SellersRancking:
    def _list_seller_name(self, sellers):
        return [s["name"] for s in sellers]

    def best_seller(self, sellers):
        return self.rancking_list(sellers)[:1]

    def rancking_list(self, sellers):
        return self._list_seller_name(
            sorted(sellers, key=itemgetter("value"), reverse=True)
        )

    def best_seller_store(self, sellers, store):
        _sellers_of_store = list(filter(lambda s: s["store"] == store, sellers))
        return self.best_seller(_sellers_of_store)

    def sales_goals(self, sellers):
        _sales_goals = list(filter(lambda s: s["value"] < GOAL, sellers))
        return self._list_seller_name(sorted(_sales_goals, key=itemgetter("value")))
