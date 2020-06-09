import query_runner
import stardog
import subprocess, os
from string import Template
import json

class SparqlQueryRunner(query_runner.QueryRunner):
    
    def __init__(self, queryPath="queries"):
        query_runner.QueryRunner.__init__(self)
        self.queryPath=queryPath

    def runQuery(self, query):
        pass
        
    def readQueryFromFile(self, filePath):
        with open(filePath, 'r') as file:
            data = file.read()
            return data

    def date(self, date):
        if len(date) != 17:
            print ('Please set the input date in format: yyyymmddhhmmssmmm')
        
        year = date[0:4]
        month = date[4:6]
        day = date[6:8]
        hour = date[8:10]
        minute = date[10:12]
        second = date[12:14]
        milli = date[14:17]

        dateTime = "xsd:datetime(\"" + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + milli + "Z\")"
        return dateTime

    def literalise(self, string):
        return "\"" + string +"\""

    def collectionise(self, elements):
        result = "(\"" + "\" \"".join(elements) + "\")"
        return result

    def i_complex_1(self, personId, firstName):
        queryFilePath=os.path.join(self.queryPath, "interactive-complex-1.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(personId=personId, firstName=self.literalise(firstName))
        return self.runQuery(qt)

    def i_complex_2(self, personId, date):
        dateTime = self.date(date)
        queryFilePath=os.path.join(self.queryPath, "interactive-complex-2.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(personId=personId, maxDate=dateTime)
        return self.runQuery(qt)
    
    def i_complex_3(self, personId, startDate, days, countryXName, countryYName):
        dateTime = self.date(startDate)

        queryFilePath=os.path.join(self.queryPath, "interactive-complex-3.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            personId=personId, 
            startDate=dateTime, 
            durationDays=self.durationDays(days), 
            countryXName=self.literalise(countryXName), 
            countryYName=self.literalise(countryYName))
        return self.runQuery(qt)

    def i_complex_4(self, personId, startDate, days):
        dateTime = self.date(startDate)
        queryFilePath=os.path.join(self.queryPath, "interactive-complex-4.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            personId=personId, 
            startDate=dateTime, 
            durationDays=self.durationDays(days))
        return self.runQuery(qt)

    def i_complex_5(self, personId, minDate):
        dateTime = self.date(minDate)
        queryFilePath=os.path.join(self.queryPath, "interactive-complex-5.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            personId=personId, 
            minDate=dateTime)
        return self.runQuery(qt)

    def i_complex_6(self, personId, tagName):
        queryFilePath=os.path.join(self.queryPath, "interactive-complex-6.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            personId=personId, 
            tagName=self.literalise(tagName))
        return self.runQuery(qt)

    def i_complex_7(self, personId):
        queryFilePath=os.path.join(self.queryPath, "interactive-complex-7.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            personId=personId)
        return self.runQuery(qt)

    def i_complex_8(self, personId):
        queryFilePath=os.path.join(self.queryPath, "interactive-complex-8.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            personId=personId)
        return self.runQuery(qt)

    def i_complex_9(self, personId, date):
        dateTime = self.date(date)
        queryFilePath=os.path.join(self.queryPath, "interactive-complex-9.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            personId=personId, 
            maxDate=dateTime)
        return self.runQuery(qt)

    def i_complex_10(self, personId, month):
        queryFilePath=os.path.join(self.queryPath, "interactive-complex-10.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            personId=personId, 
            month=month)
        return self.runQuery(qt)

    def i_complex_11(self, personId, country, workFromYear):
        queryFilePath=os.path.join(self.queryPath, "interactive-complex-11.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            personId=personId,
            countryName=self.literalise(country),
            workFromYear=workFromYear)
        return self.runQuery(qt)

    def i_complex_12(self, personId, tagClassName):
        queryFilePath=os.path.join(self.queryPath, "interactive-complex-12.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            personId=personId, 
            tagClassName=self.literalise(tagClassName))
        return self.runQuery(qt)

    def i_complex_13(self, person1Id, person2Id):
        queryFilePath=os.path.join(self.queryPath, "interactive-complex-13.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            person1Id=person1Id, 
            person2Id=person2Id)
        return self.runQuery(qt)

    def i_complex_14(self, person1Id, person2Id):
        queryFilePath=os.path.join(self.queryPath, "interactive-complex-14.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            person1Id=person1Id, 
            person2Id=person2Id)
        return self.runQuery(qt)

    def bi_1(self, date):
        dateTime = self.date(date)
        queryFilePath=os.path.join(self.queryPath, "bi-1.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            date=dateTime
            )
        return self.runQuery(qt)

    def bi_2(self, startDate, endDate, country1, country2):
        dateTime1 = self.date(startDate)
        dateTime2 = self.date(endDate)
        queryFilePath=os.path.join(self.queryPath, "bi-2.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            startDate=dateTime1,
            endDate=dateTime2,
            country1=self.literalise(country1),
            country2=self.literalise(country2))
        return self.runQuery(qt)

    def bi_3(self, year, month):
        queryFilePath=os.path.join(self.queryPath, "bi-3.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            year=year,
            month=month)
        return self.runQuery(qt)

    def bi_4(self, tagClass, country):
        queryFilePath=os.path.join(self.queryPath, "bi-4.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            country=self.literalise(country),
            tagClass=self.literalise(tagClass)
            )
        return self.runQuery(qt)

    def bi_5(self, country):
        queryFilePath=os.path.join(self.queryPath, "bi-5.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            country=self.literalise(country)
            )
        return self.runQuery(qt)

    def bi_6(self, tag):
        queryFilePath=os.path.join(self.queryPath, "bi-6.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            tag=self.literalise(tag)
            )
        return self.runQuery(qt)

    def bi_7(self, tag):
        queryFilePath=os.path.join(self.queryPath, "bi-7.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            tag=self.literalise(tag)
            )
        return self.runQuery(qt)

    def bi_8(self, tag):
        queryFilePath=os.path.join(self.queryPath, "bi-8.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            tag=self.literalise(tag)
            )
        return self.runQuery(qt)

    def bi_9(self, tagClass1, tagClass2, threshold):
        queryFilePath=os.path.join(self.queryPath, "bi-9.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            tagClass1=self.literalise(tagClass1),
            tagClass2=self.literalise(tagClass2),
            threshold=threshold
            )
        return self.runQuery(qt)

    def bi_10(self, tag, date):
        dateTime = self.date(date)
        queryFilePath=os.path.join(self.queryPath, "bi-10.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            date=dateTime,
            tag=self.literalise(tag)
            )
        return self.runQuery(qt)

    def bi_11(self, country, blocklist):
        queryFilePath=os.path.join(self.queryPath, "bi-11.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            blacklist="\"" + "| ".join(blocklist) + "\"",
            country=self.literalise(country)
            )
        return self.runQuery(qt)

    def bi_12(self, date, likeThreshold):
        dateTime = self.date(date)
        queryFilePath=os.path.join(self.queryPath, "bi-12.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            date=dateTime,
            likeThreshold=likeThreshold
            )
        return self.runQuery(qt)

    def bi_13(self, country):
        queryFilePath=os.path.join(self.queryPath, "bi-13.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            country=self.literalise(country)
            )
        return self.runQuery(qt)

    def bi_14(self, startDate, endDate):
        dateTime1 = self.date(startDate)
        dateTime2 = self.date(endDate)
        queryFilePath=os.path.join(self.queryPath, "bi-14.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            startDate=dateTime1,
            endDate=dateTime2
            )
        return self.runQuery(qt)

    def bi_15(self, country):
        queryFilePath=os.path.join(self.queryPath, "bi-15.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            country=self.literalise(country)
            )
        return self.runQuery(qt)

    def bi_16(self, personId, country, tagClass, minPathDistance, maxPathDistance):
        queryFilePath=os.path.join(self.queryPath, "bi-16.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            personId=personId,
            country=self.literalise(country),
            minPathDistance=minPathDistance,
            maxPathDistance=maxPathDistance,
            tagClass=self.literalise(tagClass)
            )
        return self.runQuery(qt)

    def bi_17(self, country):
        queryFilePath=os.path.join(self.queryPath, "bi-17.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            country=self.literalise(country)
            )
        return self.runQuery(qt)

    def bi_18(self, date, lengthThreshold, languages):
        dateTime = self.date(date)
        queryFilePath=os.path.join(self.queryPath, "bi-18.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            date=dateTime,
            languages=self.collectionise(languages),
            lengthThreshold=lengthThreshold
            )
        return self.runQuery(qt)

    def bi_19(self, date, tagClass1, tagClass2):
        queryFilePath=os.path.join(self.queryPath, "bi-19.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            date=date,
            tagClass1=self.literalise(tagClass1),
            tagClass2=self.literalise(tagClass2)
            )
        return self.runQuery(qt)

    def bi_20(self, tagClasses):
        queryFilePath=os.path.join(self.queryPath, "bi-20.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            tagClasses=self.collectionise(tagClasses)
            )
        return self.runQuery(qt)

    def bi_21(self, country, endDate):
        dateTime = self.date(endDate)
        queryFilePath=os.path.join(self.queryPath, "bi-21.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            country=self.literalise(country),
            endDate=dateTime
            )
        return self.runQuery(qt)

    def bi_22(self, country1, country2):
        queryFilePath=os.path.join(self.queryPath, "bi-22.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            country1=self.literalise(country1),
            country2=self.literalise(country2)
            )
        return self.runQuery(qt)

    def bi_23(self, country):
        queryFilePath=os.path.join(self.queryPath, "bi-23.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            country=self.literalise(country)
            )
        return self.runQuery(qt)

    def bi_24(self, tagClass):
        queryFilePath=os.path.join(self.queryPath, "bi-24.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            tagClass=self.literalise(tagClass)
            )
        return self.runQuery(qt)

    def bi_25(self,person1Id, person2Id, startDate, endDate):
        pass