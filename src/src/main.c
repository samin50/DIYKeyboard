#include <zephyr/kernel.h>
#include <zephyr/logging/log.h>
LOG_MODULE_REGISTER(my_modul);

int main(void)
{
    // write a while loop with printk to print "Hello World!" infinite times with delay of 1 second
    while(1)
    {
        k_msleep(1000);
        LOG_INF("nRF Connect SDK Fundamentals");
    }
}
