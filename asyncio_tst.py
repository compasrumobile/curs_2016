import asyncio
import logging
import concurrent.futures

@asyncio.coroutine
def handle_connection(reader, writer):
    peername = writer.get_extra_info('peername')
    logging.info('Accepted connection from {}'.format(peername))
    while True:
        try:
            data = yield from asyncio.wait_for(reader.readline(), timeout=10.0)
            if data: 
                writer.write(data)
            else:
                logging.info('Connection from {} closed by peer'.format(peername))
                break
        except concurrent.futures.TimeoutError:
            logging.info('Connection from {} closed by timeout'.format(peername))
            break
    writer.close()