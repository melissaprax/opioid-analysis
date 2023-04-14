# Written here is the psuedo code for our calculated variable: Treatment Facility Quality (TFQ)

df = pd.DataFrame(data)

# Subvariables:

a = ASSESSMENT #(0-8)
b = TESTING #(0-9)
c = TRANSITION #(0-4)
d = RECOVERY #(0-6)
e = EDUCATION #(0-10)
f = PHARMACOTHERAPIES #(0-16)

# Essentially, this model operates within "the more the merrier" paradigm. This does not stem from my education in public, but an intuitive hypotheses based on linear return to scale.

df['TFQ'] = sum(a,b,c,d,e,f)

