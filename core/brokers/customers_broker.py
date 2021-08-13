from .base_broker import Broker


class CustomersBroker(Broker):
    alias = 'customers'
    name = 'customers'

    def login(self, sub_domain: str, email: str, password: str):
        url = self.make_url('auth', 'login')
        return self.make_request(
            method='POST',
            url=url,
            json={
                'sub_domain': sub_domain,
                'email': email,
                'password': password
            }
        )

    def list_customers(self, business_id: str, params, **kwargs):
        url = self.make_url('business', business_id, 'customers')
        return self.make_request(
            method='GET',
            url=url,
            params=params,
            **kwargs
        )

    def get_customer(self, business_id: str, customer_id: str, params, **kwargs):
        url = self.make_url('business', business_id, 'customers', customer_id)
        return self.make_request(
            method='GET',
            url=url,
            params=params,
            **kwargs
        )
