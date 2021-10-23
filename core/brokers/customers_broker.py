from .base_broker import Broker


class CustomersBroker(Broker):
    alias = "customers"
    name = "customers"

    async def login(self, sub_domain: str, email: str, password: str):
        url = self.make_url("auth", "login")
        return await self.make_request(
            method="POST", url=url, json={"sub_domain": sub_domain, "email": email, "password": password}
        )

    async def list_customers(self, business_id: str, params, **kwargs):
        url = self.make_url("business", business_id, "customers")
        return await self.make_request(method="GET", url=url, params=params, **kwargs)

    async def get_customer(self, business_id: str, customer_id: str, params, **kwargs):
        url = self.make_url("business", business_id, "customers", customer_id)
        return await self.make_request(method="GET", url=url, params=params, **kwargs)

    async def create_customer(self, business_id: str, params, **kwargs):
        url = self.make_url("business", business_id, "customers")
        return await self.make_request(method="POST", url=url, params=params, **kwargs)

    async def update_customer(self, business_id: str, customer_id: str, params, **kwargs):
        url = self.make_url("business", business_id, "customers", customer_id)
        return await self.make_request(method="PUT", url=url, params=params, **kwargs)
