from .subscription.single_subscription import SingleSubscription
from .helpers.constants import Constants
from .subscription.subscription import Subscription
import json


class SubscriptionParser():

    def subscription_parser():

        subscription = Subscription('')
        single_subscription = SingleSubscription('', [], '')

        # Path to json file
        path_json = Constants.FILE_PATH

        with open(path_json, 'r') as file:
            json_string = json.load(file)

        
        for json_element in json_string:
            single_subscription.set_url(json_element['url'])
            single_subscription.set_url_type(json_element['urlType'])
            
            for url_param in json_element['urlParams']:
                single_subscription.set_ulr_param(url_param)


        param_len = single_subscription.get_ulr_params_size()
        
        for i in range(param_len):
            subscription.add_single_subscription(
                SingleSubscription(
                single_subscription.get_feed_to_request(i), 
                single_subscription.get_ulr_params(), 
                single_subscription.get_url_type())
            )
        

        return subscription
            

       



if __name__ == '__main__':
    print(SubscriptionParser.subscription_parser())
        
