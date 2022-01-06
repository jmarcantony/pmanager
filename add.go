package main

func Add(d Data, website string, addr string, pass string) Data {
	if _, ok := d[website]; !ok {
		d[website] = map[string]string{}
	}
	d[website][addr] = pass
	return d
}
