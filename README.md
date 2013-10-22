### e2j

I just need a simple API that returns a json response to my excel sheets :-)
that's all folks.


# Testing this API

Use a curl request as follows

curl --form type=@"spline" file=@/path/to/file.xlsx http://localhost:8000/upload/

Replace localhost with whatever IP address or Domain that you use.


What should the data in the excel sheet look like? (Using spline charts as examples)

1) First row defines the the "heading"

Time values ---> City  Jan Feb Mar  Apr  May  Jun
Dataset Values-> Tokyo  7  6.9 14.5 18.2 21.5 25.2
Dataset Values-> London 7  7.9 15.5 16.2 22.5 25.2

The dataset values define the series in a chart. Name versus values
Decomposition of the dataset above:

xAxis: { categories: ['Jan, 'Feb', 'Mar', 'Apr', 'May', 'Jun']}


"a collection of hash objects" makes the series

series: [
        {
         name:'Tokyo',
         marker: { symbol: 'square'},
         data: [7, 6.9, 14.5, 18.2, 21.5, 25.2]
        },
        {
         name: 'London',
         marker: { symbol: 'diamond'},
         data: [7, 7.9, 15.5, 16.2, 22.5, 25.2]
        }
        ]

For the use of the different graphs; the excel sheet has to be designed in a
specific way; there is only so much that "artificial inteligence" can offer;
in the same spirit of "formhub", a programmer/manager/data entry person can
upload to this API using a particular format.
