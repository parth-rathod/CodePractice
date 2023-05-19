## Encoding Techniques

1.   Dictionary Encoding:
        
        These are the steps taken by Dictionary Encoding:

            a. Each of the distinct values per column are extracted into a dictionary (lookup table) and given a numerical index.

            b. Initial values in the column are replaced by these indexes and are later mapped via the lookup dictionary.

        ![Dictionary Encoding](/CodeExamples/Data_Engineering/images/dictionary_encoding.png)

        When does it make sense to use Dictionary Encoding?

        a. The data in the column is of low enough cardinality.



2. Run Length Encoding:

        a. Table columns are scanned for sequence of repeated values.

        b. Sequence of repeated values is transformed into object containing two values:

                Number of times the value was repeated sequentially.

                The value itself.

                The column is then transformed into sequence of these two value objects.
        
    ![RLE Encoding](/CodeExamples/Data_Engineering/images/rle.png)

3. Combining Dictionary Encoding and RLE:

    Given the ideal scenario when the data is fully ordered in each column, it would not make sense to use anything other than RLE, however this is never the case in the real world as you will have to order the column sequentially which will reduce the orderliness of values each time we sort.

            a. Apply dictionary encoding on the column.

            b. Apply RLE encoding on the resulting column using the index values in the column that was result of the previous step.

    ![Combine Encoding](/CodeExamples/Data_Engineering/images/combine_dic_rle.png)

4. Delta Encoding:

    One more encoding technique that is often overlooked is called Delta Encoding. 
    
        a. Record the first value of the column.

        b. Calculate the difference between the current value and the previous value and save it as record representation.

        c. Move to the next record in the column and apply the previous procedure.

        d. Continue until you reach the end of the column.
    
    ![Delta Encoding](/CodeExamples/Data_Engineering/images/delta_encoding.png)