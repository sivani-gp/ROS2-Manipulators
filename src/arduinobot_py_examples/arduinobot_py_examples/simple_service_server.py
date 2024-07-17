import rclpy
from rclpy.node import Node
from arduinobot_msgs.srv import Addtwoints 


class SimpleServiceServer(Node):
    def __init__(self):
        super().__init__("simple_service_server")

        self.service_ = self.create_service(Addtwoints,"add_two_ints", self.serviceCallback)
        self.get_logger().info("Service add_two_ints Ready")

    def serviceCallback(self, req, res):
        self.get_logger.info("New Message recieved a: %d, b: %d" % (req.a,req.b))
        res = req.a+req.b
        self.get_logger().info("Returning sum: %d" %res.sum)
        return res
    
def main():
    rclpy.init()
    simple_service_server = SimpleServiceServer()
    rclpy.spin(simple_service_server)
    simple_service_server.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    