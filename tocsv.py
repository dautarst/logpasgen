export_data = zip_longest(*lppair)
with open('users.csv', 'w') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("login","password"))
      wr.writerows(export_data)
myfile.close()



trans_lppair = [[lppair[j][i] for j in range (len(lppair))] for i in range (len(lppair[0]))];




trans_lppair = [[lppair[j][i] for j in range (len(lppair))] for i in range (len(lppair[0]))];
print(trans_lppair)
result = pd.DataFrame([trans_lppair]);
new_columns = ['login','password']
print(result)
result.to_csv('users.csv', index=False, sep=',');