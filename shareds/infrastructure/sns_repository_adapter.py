import boto3
from botocore.exceptions import ClientError

class SNSRepositoryAdapter:
    """
    Adapter for interacting with AWS SNS (Simple Notification Service).

    This class provides methods for creating SNS topics, managing email subscriptions,
    and publishing messages to subscribers. It acts as an interface between the application
    and the AWS SNS service.

    Attributes:
        topic_arn (str): The ARN (Amazon Resource Name) for the SNS topic.
    """

    def sns_client(self):
        """
        Creates and returns an SNS client using Boto3.

        This method initializes the Boto3 SNS client with the region 'us-east-1'.
        If an error occurs during client creation, it returns an error message.

        Returns:
            boto3.client: An instance of the Boto3 SNS client.
            print An error message if the client creation fails.
            return None
        """
        try:
            return boto3.client("sns", region_name="us-east-1")
        except ClientError as e:
            return f"Error: {e}"

    def create_user_topic(self, user_id: int):
        """
        Creates an SNS topic with the specified user id.

        This method uses the `topic_arn` attribute to create a new SNS topic.
        If an error occurs during topic creation, it returns an error message.

        Returns:
            dict: The response from the SNS client upon creating the topic.
            print an error message if the topic creation fails.
            return None
        """
        try:
            response = self.sns_client().create_topic(Name=f"user_{user_id}_topic")
            return response["TopicArn"]
        except ClientError as e:
            print(f"Error creating topic: {e}")
            return None

    def create_email_subscription(self, topic_arn: str, email_address: str):
        """
        Creates an email subscription for the specified SNS topic.

        This method subscribes an email address to the given SNS topic ARN.
        If an error occurs during subscription, it returns an error message.

        Args:
            topic_arn (str): The ARN of the SNS topic to subscribe to.
            email_address (str): The email address to subscribe.

        Returns:
            dict: The response from the SNS client upon creating the subscription.
            return: None, and print An error message if the subscription creation fails.

        """
        try:
            return self.sns_client().subscribe(
                TopicArn=topic_arn, Protocol="email", Endpoint=email_address
            )
        except ClientError as e:
            print(f"Error subscribing email: {e}")
            return None

    def get_subscription_arn(self, email: str):
        """
        Retrieves the ARN of the subscription associated with the given email address.

        This method lists all SNS subscriptions and searches for a subscription
        with the specified email address. If found, it returns the subscription ARN.
        If an error occurs during the retrieval, it returns an error message.

        Args:
            email (str): The email address to find the subscription for.

        Returns:
            str: The ARN of the subscription if found.
            None: If no subscription is found for the email.
            str: An error message if an error occurs during retrieval.
        """
        try:
            response = self.sns_client().list_subscriptions()
            for subscription in response.get("Subscriptions", []):
                if (
                    subscription["Protocol"] == "email"
                    and subscription["Endpoint"] == email
                ):
                    return subscription["TopicArn"]
            return None
        except ClientError as e:
            return f"Error: {e}"

    def publish_message_to_subscriber(self, email: str, message: str):
        """
        Publishes a message to the subscriber associated with the given email address.

        This method retrieves the subscription ARN for the specified email address
        and publishes the given message to that subscription. If the subscription
        is not found or an error occurs during publishing, it returns an appropriate message.

        Args:
            email (str): The email address of the subscriber.
            message (str): The message to publish.

        Returns:
            dict: The response from the SNS client upon publishing the message.
            return None if error and print an error message if the subscription is not found or publishing fails.
        """
        subscription_arn = self.get_subscription_arn(email)
        if subscription_arn:
            try:
                response = self.sns_client().publish(
                    TargetArn=subscription_arn,
                    Message=message,
                )
                return response
            except ClientError as e:
                print(f"Error: {e}") 
        return None
