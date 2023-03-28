import resolver as r
import file_consumer
import file_producer
import store as s
import service as svc


def producer_consumer(resolver: r.ExportPathResolver):
    producer = file_producer.FileProducer("files/")

    consumer = file_consumer.FileConsumer("exported1/", resolver)

    for file_tuple in producer.produce():
        consumer.consume(file_tuple)


def daw_service(resolver: r.ExportPathResolver):
    store = s.GroupedFileStore()

    service = svc.FileGroupingService(store, resolver)
    service.groupFiles("exported/", "files/")


def main():
    
    resolver = r.ByLanguageDirResolver()
    
    # solution 1
    producer_consumer(resolver)
    
    # solution 2
    daw_service(resolver)


if __name__ == "__main__":
    main()
