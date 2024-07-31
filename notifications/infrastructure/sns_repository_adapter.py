import boto3
from botocore.exceptions import ClientError


class SNSRepositoryAdapter:

    def __init__(self, topic_arn):
        self.topic_arn = topic_arn

    def sns_client(self):
        try:
            return boto3.client("sns", region_name="us-east-1")
        except ClientError as e:
            return f"Error: {e}"

    def create_topic(self):
        try:
            return self.sns_client().create_topic(Name=self.topic_arn)
        except ClientError as e:
            return f"Error: {e}"

    def create_email_subscription(self, topic_arn, email_address):
        try:
            return self.sns_client().subscribe(
                TopicArn=topic_arn, Protocol="email", Endpoint=email_address
            )
        except ClientError as e:
            return f"Error: {e}"

    def get_subscription_arn(self, email):
        try:
            response = self.sns_client().list_subscriptions()
            for subscription in response.get("Subscriptions", []):
                if (
                    subscription["Protocol"] == "email"
                    and subscription["Endpoint"] == email
                ):
                    return subscription["SubscriptionArn"]
            return None
        except ClientError as e:
            return f"Error: {e}"

    def publish_message_to_subscriber(self, email, message):
        subscription_arn = self.get_subscription_arn(email)
        if subscription_arn:
            try:
                response = self.sns_client().publish(
                    TargetArn=subscription_arn,
                    Message=message,
                )
                return response
            except ClientError as e:
                return f"Error: {e}"
        else:
            return "Subscription not found"
