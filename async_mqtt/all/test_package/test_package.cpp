#include <boost/asio.hpp>
#include <async_mqtt/all.hpp>

int main() {
    async_mqtt::setup_log();

    boost::asio::io_context ioc;

    auto c = async_mqtt::client<async_mqtt::protocol_version::v3_1_1, async_mqtt::protocol::mqtt>::create(ioc.get_executor());//, "localhost", "40000");


    //c->set_client_id("test_package");
    //c->set_clean_session(true);

    return 0;
}
