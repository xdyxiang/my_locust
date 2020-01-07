package main

import "time"
import "github.com/myzhan/boomer"

func foo(){
    start := time.Now()
    time.Sleep(100 * time.Millisecond)
    elapsed := time.Since(start)

    /*
    Report your test result as a success, if you write it in locust, it will looks like this
    events.request_success.fire(request_type="http", name="foo", response_time=100, response_length=10)
    */
    boomer.RecordSuccess("http", "foo", elapsed.Nanoseconds()/int64(time.Millisecond), int64(10))
}

func bar(){
    start := time.Now()
    time.Sleep(100 * time.Millisecond)
    elapsed := time.Since(start)

    /*
    Report your test result as a failure, if you write it in locust, it will looks like this
    events.request_failure.fire(request_type="udp", name="bar", response_time=100, exception=Exception("udp error"))
    */
    boomer.RecordFailure("udp", "bar", elapsed.Nanoseconds()/int64(time.Millisecond), "udp error")
}

func main(){
    task1 := &boomer.Task{
        Name: "foo",
        // The weight is used to distribute goroutines over multiple tasks.
        Weight: 10,
        Fn: foo,
    }

    task2 := &boomer.Task{
        Name: "bar",
        Weight: 20,
        Fn: bar,
    }

    boomer.Run(task1, task2)
}

// https://github.com/myzhan/boomer
