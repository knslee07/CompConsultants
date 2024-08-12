# TRAIN_DATA.py is the py file to store train examples for compensation consultants.
# automate creating training examples 
# Adapted from Ch. 10 of NLP with Spacy

# you can automate creating examples applying this. See compensationConsultantsInfo.xlsx
# you can add the list of organizations so that it does not classify as CC.
# automate creating training examples
'''
import spacy
nlp=spacy.load('en_core_web_trf')
doc=nlp("In addition to the assistance provided by Biogen Idec’s internal Compensation and Benefits group, the Committee currently engages Frederic W. Cook & Co., Inc (Cook) as an independent compensation consultant. Cook replaced Watson Wyatt Worldwide (Watson Wyatt) in this role in July 2009.")

### alternatively, use a file to load a doc obj.
# f=open('file.txt', 'rb')
# contents=f.read()
# doc-nlp(contents.decode('utf8'))

CC=['Deloitte','Aon','Aon Hewitt','Compensation Advisory Partners','Mercer HR Consulting',
   'Hewitt','Compensia','Exequity','FPL Advisory Group Co.','Frederic W. Cook & Co., Inc.', 'Frederic W. Cook & Co.','F.W. Cook','F. W. Cook', 'Cook & Co.',
    'FTI Consulting Inc.','Hay Group', 'The Hay Group','Hewitt Associates','Longecker & Associates',
    'Mercer','Mercer Human Resources Consulting','Mercer Human Resource Consulting','Meridian','Meridian Compensation',
    'Pay Governance','Pearl Meyer & Partners','Radford','Semler Brossy Consulting',
    'Semler Brossy','Steven Hall & Partners','Towers Watson','Watson Wyatt','Towers Perrin','Watson Wyatt Worldwide',
    'CCA Strategies','Total Rewards Strategies']

train_exams=[]
for sent in doc.sents:
    entities=[]
    for token in sent:
        if token.ent_type!=0:
            start=token.idx - sent.start_char  # The serious problem with this is it does not do well with noun chunks!!!
            if token.text in CC:
                entity=(start, start+len(token), 'CC')
            else:
                entity = (start, start+len(token), token.ent_type_)
            entities.append(entity)
    tpl=(sent.text, {'entities': entities})
    train_exams.append(tpl) 
'''
    
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

TRAIN_DATA = [
    (
        'F.W. Cook has not provided any other services to the Company and has received no compensation other than with respect to the services provided to the Committee.',
  {'entities': [(0, 9, 'CC')]}
  ),
 ('The committee has engaged Hewitt Associates to provide counsel and advice on executive and non-employee director compensation matters.',
  {'entities': [(26, 43, 'CC')]}),
 ('Hewitt, and its principal, report directly to the chair of the committee.',
  {'entities': [(0, 6, 'CC')]}),
 ('The principal meets regularly, and as needed, with the committee in executive sessions, has direct access to the chair during and between meetings, and performs no other services for Abbott or its senior executives.',
  {'entities': []}),
 ("The committee determines what variables it will instruct Hewitt to consider, and they include: peer groups against which performance and pay should be examined, financial metrics to be used to assess Abbott's relative performance, competitive long-term incentive practices in the market place, and compensation levels relative to market practice.",
  {'entities': [(57, 63, 'CC')]}),
 ('The committee negotiates and approves any fees paid to Hewitt for these services.',
  {'entities': [(55, 61, 'CC')]}),
 ('In 2008, the committee authorized payment of approximately $239,109 to Hewitt for services rendered to the committee relating to executive compensation.',
  {'entities': [(71, 77, 'CC')]}),
 ('Separately, Abbott paid approximately $5.3 million for unrelated services, including actuarial work, pension design and administration, and general consulting.',
  {'entities': []}),
 ('The committee has engaged Aon Hewitt to provide counsel and advice on executive and non-employee director compensation matters.  ',
  {'entities': [(26, 36, 'CC')]}),
 ('The Committee engaged Aon Hewitt as its compensation consultant for 2013.',
  {'entities': [(22, 32, 'CC')]}),
 ('For 2014, the Compensation Committee has selected a new Compensation Committee consultant, Meridian, whose company performs no other work for Abbott.',
  {'entities': [(91, 99, 'CC')]}),
 ('Separately, Abbott management engaged Aon Hewitt to perform and paid approximately $5.8 million for unrelated services, including actuarial work, pension design and administration, insurance, and general consulting.',
  {'entities': [(38, 48, 'CC')]}),
 ('The Committee engaged Meridian.', {'entities': [(22, 30, 'CC')]}),
 ('The Committee engages compensation consultants to provide counsel and advice on executive and non-employee director compensation matters.',
  {'entities': []}),
 ('The consultant and its principal report directly to the Chair of the Committee.',
  {'entities': []}),
 ('The principal meets regularly and as needed with the Committee in executive sessions, has direct access to the Chair during and between meetings, and performs no other services for Abbott or its senior executives.',
  {'entities': []}),
 ("The Committee determines what variables it will instruct the consultant to consider, and they include: peer groups against which performance and pay should be examined, financial metrics to be used to assess Abbott's relative performance, competitive long-term incentive practices in the marketplace, and compensation levels relative to market practice.",
  {'entities': []}),
 ('The Committee negotiates and approves any fees paid to the consultant for these services.',
  {'entities': []}),
 ("Based on its evaluation of Meridian's independence in accordance with the New York Stock Exchange listing standards and information provided by Meridian, the Committee determined that the work performed by Meridian does not present any conflicts of interest.",
  {'entities': [(144, 152, 'CC')]}),
 ("Based on its evaluation of Meridian's independence in accordance with the New York Stock Exchange listing standards and information provided by Meridian, the Committee determined that the work performed by Meridian does not present any conflicts of interest.",
  {'entities': [(206, 214, 'CC')]}),
 ('The Committee engaged Meridian as its compensation consultant for 2015.',
  {'entities': [(22, 30, 'CC')]}),
 ('Meridian performs no other work for Abbott.', {'entities': [(0, 8, 'CC')]}),
 ('The Committee has retained Mercer Human Resource Consulting (Mercer) as its consultant in order to have access to objective, expert perspectives on matters related to executive compensation.',
  {'entities': [(27, 59, 'CC')]}),
 ('The Committee has retained Mercer Human Resource Consulting (Mercer) as its consultant in order to have access to objective, expert perspectives on matters related to executive compensation.',
  {'entities': [(61, 67, 'CC')]}),
 ('Mercer was selected as the consultant to the Committee in 2004 after an interview process with executive compensation consulting firms.',
  {'entities': [(0, 6, 'CC')]}),
 ('In 2006, Mercer advised the Committee on a variety of compensation-related issues, including compensation strategy, plan design, executive and Board member compensation levels, and preparation of the CompensationIn 2009, the Compensation Committee retained Semler Brossy as its consultant in order to get objective, expert advice.',
  {'entities': [(9, 15, 'CC')]}),
 ('In 2006, Mercer advised the Committee on a variety of compensation-related issues, including compensation strategy, plan design, executive and Board member compensation levels, and preparation of the CompensationIn 2009, the Compensation Committee retained Semler Brossy as its consultant in order to get objective, expert advice.',
  {'entities': [(257, 270, 'CC')]}),
 ('Semler Brossy was selected as the consultant to the Compensation Committee in 2008 after an interview process with several compensation consulting firms.',
  {'entities': [(0, 13, 'CC')]}),
 ('In September 2010, the Compensation Committee retained Compensia, Inc. as its compensation consultant.',
  {'entities': [(55, 64, 'CC')]}),
 ('During fiscal 2015, the Compensation Committee retained Compensia, Inc. (“Compensia”),',
  {'entities': [(56, 65, 'CC')]}),
 ('a national compensation consulting firm, as its independent compensation consultant to provide assistance on executive and director compensation matters.',
  {'entities': []}),
 ('Compensia advised the Compensation Committee on a variety of compensation-related matters in fiscal 2015, including: The Committee may engage compensation consultants but did not do so in 2006.',
  {'entities': [(0, 9, 'CC')]}),
 ('Additional information on the Committee’s processes and procedures for considering and determining executive compensation is contained in the “Compensation Discussion and Analysis” section of this Proxy Statement.',
  {'entities': []}),
 ('The Committee may engage compensation consultants but did not do so in 2007.',
  {'entities': []}),
 ('Additional information on the Committee’s processes and procedures for considering and determining executive compensation is contained in the “Compensation Discussion and Analysis” section of this Proxy Statement.',
  {'entities': []}),
 ('The Committee has the authority to retain and terminate any independent, third-party compensation consultant and to obtain advice and assistance from internal and external legal, accounting and other advisors.',
  {'entities': []}),
 ('Since 2014, the Compensation Committee has engaged the services of Pay Governance LLC (“Pay Governance”), an independent executive compensation consulting firm.',
  {'entities': []}),
 ('During 2015, Pay Governance did not provide any other services to Apple and worked with Apple’s management, as directed by the Compensation Committee, only on matters for which the Compensation Committee is responsible.',
  {'entities': [(13, 27, 'CC')]}),
 ('In 2014, the Compensation Committee selected and directly retained the services of Pay Governance LLC, an independent executive compensation consulting firm.',
  {'entities': []}),
 ('Pay Governance did not provide any other services to the Company and worked with the Company’s management, as directed by the Compensation Committee, only on matters for which the Compensation Committee is responsible.',
  {'entities': [(0, 14, 'CC')]}),
 ('The Compensation Committee assessed the independence of Pay Governance pursuant to SEC and NASDAQ rules and concluded that no conflict of interest exists that would prevent Pay Governance from serving as an independent consultant to the Compensation Committee.',
  {'entities': [(56, 70, 'CC')]}),
 ('The Compensation Committee assessed the independence of Pay Governance pursuant to SEC and NASDAQ rules and concluded that no conflict of interest exists that would prevent Pay Governance from serving as an independent consultant to the Compensation Committee.',
  {'entities': [(173, 187, 'CC')]}),
 ('From time to time, the Committee engages CCA Strategies LLC, an employee benefits 6 and compensation consulting firm (which also acts as a consultant to the Human Resources Committee on executive compensation matters), to provide the Committee with information regarding director compensation paid by companies principally in the Fortune 50, Fortune 100 and a special comparator group used by the Human Resources Committee.',
  {'entities': []}),
 ('The Committee has selected Total Rewards Strategies to serve as its independent consultant.',
  {'entities': [(27, 51, 'CC')]}),
 ('The consultant reports directly to the Committee.', {'entities': []}),
 ('Total Rewards Strategies provides no other services to AT&T.From time to time, the Committee engages Total Rewards Strategies, LLC, an employee benefits and compensation consulting firm (which also acts as a consultant to the Human Resources Committee on executive compensation matters), to provide the Committee with information regarding director compensation paid by other public companies.',
  {'entities': [(0, 24, 'CC')]}),
 ('Total Rewards Strategies provides no other services to AT&T.From time to time, the Committee engages Total Rewards Strategies, LLC, an employee benefits and compensation consulting firm (which also acts as a consultant to the Human Resources Committee on executive compensation matters), to provide the Committee with information regarding director compensation paid by other public companies.',
  {'entities': [(101, 125, 'CC')]}),
 ('In 2011, Meridian served as the Compensation Committee’s outside compensation consultant.',
  {'entities': [(9, 17, 'CC')]}),
 ('Meridian was retained by, and reported directly to, the Compensation Committee during its engagement as compensation consultant.',
  {'entities': [(0, 8, 'CC')]}),
 ('As outside compensation consultant, Meridian provided the following services and information to the Compensation Committee',
  {'entities': [(36, 44, 'CC')]}),
 (':The Compensation Committee has engaged an external executive compensation consulting firm, Mercer HR Consulting, to advise it on matters including, but not limited to, annual adjustments to Senior Officer pay levels, market practices regarding incentive plan design, and employment contracts, among other matters.',
  {'entities': [(92, 112, 'CC')]}),
 ('The Compensation Committee has the sole authority to continue or terminate its relationship with Mercer.',
  {'entities': [(97, 103, 'CC')]}),
 ('The Committee has retained Semler Brossy to advise on our executive compensation programs.',
  {'entities': [(27, 40, 'CC')]}),
 ('Aside from services to the Committee and other Board members, Semler Brossy performs no other services for us.',
  {'entities': [(62, 75, 'CC')]}),
 ('In 2010, Semler Brossy provided no services to the Company apart from work performed for the Committee and the Committee has determined that Semler Brossy is independent.',
  {'entities': [(9, 22, 'CC')]}),
 ('In 2010, Semler Brossy provided no services to the Company apart from work performed for the Committee and the Committee has determined that Semler Brossy is independent.',
  {'entities': [(141, 154, 'CC')]}),
 ('A consultant is considered not independent if it provides significant services to the Company apart from work performed for the Committee (services in excess of $50,000 or 1% of the consulting firm',
  {'entities': []}),
 ('’s gross revenues for the most recent fiscal year).', {'entities': []}),
 ('In 2009, the Committee determined that Semler Brossy is independent.',
  {'entities': [(39, 52, 'CC')]}),
 ('The Compensation Committee has directly engaged George B. Paulin, Chairman and Chief Executive Officer of Frederic W. Cook& Co., Inc. as its compensation consultant.',
  {'entities': []}),
 ('Mr.Paulin reports directly to the Committee and is responsible for reviewing Committee materials, attending Committee meetings, assisting the Committee with program design and generally providing advice and counsel to the Committee as compensation issues arise.',
  {'entities': []}),
 ('The Committee also looks to Mr.Paulin for assistance in determining the competitiveness of Baxter’s total compensation structure.',
  {'entities': []}),
 ('From time to time, Hewitt Associates assists the Committee with the compilation of market data.',
  {'entities': [(19, 36, 'CC')]}),
 ('Additionally, Aon Hewitt assists the Compensation Committee with the compilation of market data from time to time.',
  {'entities': [(14, 24, 'CC')]}),
 ('Mr. Paulin reports directly and exclusively to the Compensation Committee and his firm provides no other services to Baxter except advising on executive and Board compensation matters.',
  {'entities': []}),
 ('He provides analyses and recommendations that inform the Compensation Committee’s decisions, but he does not decide or approve any compensation actions.',
  {'entities': []}),
 ('During 2015, he advised the Compensation Committee Chairman on setting agenda items for Compensation Committee meetings; reviewed management proposals presented to the Compensation Committee; assisted in the Compensation Committee’s assessment of Baxter’s compensation policies and practices (and those established for Baxalta prior to the Baxalta spin-off); and conducted a review of the compensation of non-employee directors at Baxter’s peer companies.',
  {'entities': []}),
 ('This group, which was engaged by the Committee, works with the Committee (including the Subcommittee) and management to assure the Committee and Subcommittee that executive compensation is competitive and appropriate in view of our goals.',
  {'entities': []}),
 ('The Committee periodically undertakes a comprehensive review of our compensation programs.',
  {'entities': []}),
 ('The last such review was completed at the start of fiscal 2007 when we reviewed the form of executive officer employment agreements.',
  {'entities': []}),
 ('Currently these relate to global pension actuarial and investment services as well as other global retirement plan and compensation consulting services.',
  {'entities': []}),
 ('We have not engaged a separate consultant for purposes of executive compensation.',
  {'entities': []}),
 ('The Committee has engaged Semler Brossy as its consultant for executive compensation.',
  {'entities': [(26, 39, 'CC')]}),
 ('The Committee determined that Semler Brossy is free of conflicts of interest.',
  {'entities': [(30, 43, 'CC')]}),
 ('The consultant reports directly to the Committee and works with the Committee (and the Subcommittee) and management to, among other things, provide advice regarding compensation structures in general and competitive compensation data.',
  {'entities': []}),
 ('The consultant also reviews information prepared by management for the Committee and/or Subcommittee.',
  {'entities': []}),
 ('All of the decisions with respect to determining the amount or form of executive compensation under our executive compensation programs are made by the Committee or Subcommittee alone and may reflect factors and considerations other than the information and advice provided by the consultant.',
  {'entities': []}),
 ('No other services were provided by Semler Brossy to the Committee, Subcommittee, or Company.',
  {'entities': [(35, 48, 'CC')]}),
 ('The Company engaged separate consultants, Towers Watson and The Hay Group, to supplement its internal resources and assist with compensation matters in general and with executive compensation as well.',
  {'entities': [(42, 55, 'CC'),(60, 73, 'CC')]}),
 ('Until September 2009, a small group of consultants within Mercer, Inc. ("Mercer") had served as the Compensation Committee\'s executive compensation consultant for a number of years.',
  {'entities': [(58, 64, 'CC')]}),
 ('In September 2009, members of the group left Mercer and formed Compensation Advisory Partners ("CAP"), which is now the firm engaged by, and reporting directly to, the Compensation Committee.',
  {'entities': [(45, 51, 'CC'), (63, 93, 'CC')]}),
 ('While at Mercer, the group was engaged by, and reported directly to, the Committee without input from management.',
  {'entities': [(9, 15, 'CC')]}),
 ('The consultants, when they were at Mercer and now at CAP, work with the Committee (including the Subcommittee) and management and, among other things, provide advice regarding compensation structures generally and competitive compensation data and review for the Committee and/or Subcommittee information prepared by management.',
  {'entities': [(35, 41, 'CC')]}),
 ("All of the decisions with respect to determining the amount or form of executive compensation under the Company's executive compensation programs are made by the Committee or Subcommittee alone and may reflect factors and considerations other than the information and advice provided by the consultants.",
  {'entities': []}),
 ('The Committee periodically undertakes a comprehensive review of our compensation programs.',
  {'entities': []}),
 ('During fiscal 2009, the Committee and Subcommittee considered improvements to the programs for fiscal 2010 to make them more consistent with the fiscal 2013 strategy.',
  {'entities': []}),
 ('The Committee had been aware that during the engagement of Mercer other consultants and employees within Mercer and its affiliates provided a range of consulting and other services to us.',
  {'entities': [(105, 111, 'CC')]}),
 ('Neither the Committee nor the Board of Directors approved the additional services, which related to global pension actuarial and investment services, global retirement plan and compensation consulting services and insurance brokerage services.',
  {'entities': []}),
 ('For fiscal 2010, fees paid to Mercer for executive compensation consulting services amounted to $40,000.',
  {'entities': [(30, 36, 'CC')]}),
 ('No fees were paid for director compensation services.', {'entities': []}),
 ('Fees paid to Mercer and its affiliates for other services amounted to $4.1 million.',
  {'entities': [(13, 19, 'CC')]}),
 ('As previously noted, the Committee and Subcommittee are no longer using Mercer as a consultant.',
  {'entities': [(72, 78, 'CC')]}),
 ('In order to supplement its internal resources and to help the Committee and Subcommittee as necessary, the Company has engaged a separate consultant, Towers Watson, to assist with compensation matters in general and with executive compensation as well.',
  {'entities': [(150, 163, 'CC')]}),
 ('The Compensation Committee has engaged Compensation Advisory Partners ("CAP") as its consultant for executive compensation purposes.',
  {'entities': [(39, 69, 'CC')]}),
 ("All of the decisions with respect to determining the amount or form of executive compensation under the Company's executive compensation programs are made by the Committee or Subcommittee alone and may reflect factors and considerations other than the information and advice provided by the consultants.",
  {'entities': []}),
 ('In order to supplement its internal resources and to help the Committee and Subcommittee as necessary, the Company has engaged a separate consultant, Towers Watson, to assist with compensation matters in general and with executive compensation as well.',
  {'entities': [(150, 163, 'CC')]}),
 ('The Compensation Committee has engaged Semler Brossy as its consultant for executive compensation beginning in January 2013.',
  {'entities': [(39, 52, 'CC')]}),
 ('The Committee determined that Semler Brossy is free of conflicts of interest.',
  {'entities': [(30, 43, 'CC')]}),
 ('Semler Brossy replaced Compensation Advisory Partners ("CAP"), which had been the Committee\'s consultant for a number of years, including the start of fiscal 2013.',
  {'entities': [(0, 13, 'CC')]}),
 ('Semler Brossy replaced Compensation Advisory Partners ("CAP"), which had been the Committee\'s consultant for a number of years, including the start of fiscal 2013.',
  {'entities': [(23, 53, 'CC')]}),
 ('The consultants report directly to the Compensation Committee and work with both the Committee (including the Subcommittee) and management to, among other things, provide advice regarding compensation structures in general and competitive compensation data.',
  {'entities': []}),
 ('They also review for the Committee and/or Subcommittee information prepared by management.',
  {'entities': []}),
 ('All of the decisions with respect to determining the amount or form of executive compensation under our executive compensation programs are made by the Committee or Subcommittee alone and may reflect factors and considerations other than the information and advice provided by the consultants.',
  {'entities': []}),
 ('The Company engaged a separate consultant, Towers Watson, to supplement its internal resources and assist with compensation matters in general and with executive compensation as well.',
  {'entities': [(43, 56, 'CC')]}),
 ('ExxonMobil management uses different consulting firms to advise on ExxonMobil’s general employee compensation and benefit programs.',
  {'entities': []}),
 ('The Consultant reviews Compensation Committee materials prior to Compensation Committee meetings and provides a summary of the review along with recommendations to the committee Chair.',
  {'entities': []}),
 ('The Consultant also attends Compensation Committee meetings when requested by the committee Chair.',
  {'entities': []}),
 ('Our Compensation Committee uses Watson Wyatt Worldwide (“Watson Wyatt”) as its compensation consultant.',
  {'entities': [(32, 54, 'CC')]}),
 ('Our Compensation Committee uses Watson Wyatt Worldwide (“Watson Wyatt”) as its compensation consultant.',
  {'entities': [(57, 69, 'CC')]}),
 ('As requested by the committee, Watson Wyatt advises the Compensation Committee on general marketplace trends in executive compensation, makes proposals for executive compensation programs, recommends peer companies for inclusion in competitive market analyses of compensation, and responds to other requests from the Compensation Committee for advice or resources regarding the compensation of our chief executive officer and our other named executive officers.',
  {'entities': [(31, 43, 'CC')]}),
 ('Watson Wyatt also provides input for the Compensation Committee to consider regarding the final compensation package of our chief executive officer, as discussed under “Compensation Discussion and Analysis—Cash Compensation—Mr. Green.”',
  {'entities': [(0, 12, 'CC')]}),
 ('F.W. Cook has not provided any other services to the Company and has received no compensation other than with respect to the services provided to the Committee.',
  {'entities': [(0, 9, 'CC')]})
,('The Committee engaged Frederic W. Cook & Co., Inc. (Cook & Co.) in order to advise on compensation matters.',
{'entities': [(22, 50, 'CC')]})
,("Based on its evaluation of Meridian's independence in accordance with the New York Stock Exchange listing standards and information provided by Meridian, the Committee determined that the work performed by Meridian does not present any conflicts of interest.",
  {'entities': [(27,35,'CC'), (144, 152, 'CC'), (206, 214, 'CC')]}),
("With respect to AMD’s 2010 executive compensation program, Compensia’s role was limited to reviewing the amount of each of the Named Executive Officer’s 2010 cash performance bonus and assessing the competitiveness of such bonus payment.",
 {'entities': [(59,68,'CC')]}),
('In 2010, neither Semler Brossy nor Compensia provided any services to AMD, or received any payments from AMD, other than in their capacity as a consultant to the Compensation Committee.',
  {'entities': [(17,30,'CC'),(35, 44, 'CC')]})
,('From time to time, the Committee engages CCA Strategies LLC, an employee benefits 6 and compensation consulting firm (which also acts as a consultant to the Human Resources Committee on executive compensation matters), to provide the Committee with information regarding director compensation paid by companies principally in the Fortune 50, Fortune 100 and a special comparator group used by the Human Resources Committee.' ,
 {'entities': [(41,59,'CC')]}
 ),("The Compensation Committee has directly engaged George B. Paulin, Chairman and Chief Executive Officer of Frederic W. Cook & Co., Inc. as its compensation consultant.",
 {'entities': [(106,134,'CC')]} 
 ),("The Compensation Committee has the sole and direct responsibility for the appointment, compensation and oversight of the work of any advisor retained by the Compensation Committee, and it has directly engaged George B. Paulin, Chairman and Chief Executive Officer of Frederic W. Cook & Co., Inc. (Cook & Co.), as its independent compensation consultant."
 , {'entities': [(267,295,'CC'),(297,307,'CC')]}
 ),("He also assisted in the identification of new peer companies for Baxter, in advance of the Baxalta spin-off. In accordance with the rules of the SEC and the NYSE regarding the independence of compensation consultants, Mr. Paulin provided the Compensation Committee information regarding any personal, financial, or business relationships between Cook & Co. and Baxter, its management or the members of the Compensation Committee that could impair its independence or present a conflict of interest."
, {'entities': [(346,356,'CC')]}
),("Based on its review of this information, the Compensation Committee determined that there were no relationships that impair the independence or create a conflict of interest between Baxter and Cook & Co. and the partners, consultants and employees who provide services to the Compensation Committee."
 , {'entities': [(193,203,'CC')]}
),("In addition, the Compensation Committee annually reviews the substantive performance of Mr. Paulin and Cook & Co. as part of its engagement process.",
{'entities': [(103,113,'CC')]}
 ),("A small group of consultants within Mercer Human Resource Consulting (Mercer) has served as the Compensation Committee's executive compensation consultant for a number of years."
 , {'entities': [(36,68,'CC'),(70,76,'CC')]}
 ),("The Committee is aware that other consultants and employees within Mercer provide, and have in the past provided, a range of consulting services to us."
 , {'entities': [(67,73,'CC')]})
,("The consultants from CAP report directly to the Compensation Committee and work with both the Committee (including the Subcommittee) and management to, among other things, provide advice regarding compensation structures in general and competitive compensation data. They also review for the Committee and/or Subcommittee information prepared by management.",
 {'entities': [(21,24,'CC')]})
,("No other services were provided by CAP to the Compensation Committee or to management.",
 {'entities': [(35,38,'CC')]})
,('No other services were provided by Semler Brossy or CAP to the Compensation Committee or to management.',
  {'entities': [(35, 48, 'CC'), (52,55,'CC')]})
,("The Committee utilizes the expertise of an external consultant, Pearl Meyer & Partners, whom the Committee retains and works with during the year and who provides insight into compensation trends and issues.",
 {'entities': [(64, 86, 'CC')]})
,("Pearl Meyer & Partners does not provide other services to ExxonMobil beyond supporting the Committee and assisting the Board Affairs Committee on non-employee director compensation."
 , {'entities': [(0,22, 'CC')]})
,("The Chair of the Compensation Committee negotiates the terms of Pearl Meyer & Partners’ engagement."
 , {'entities': [(64, 86, 'CC')]})
,("The Committee uses an independent consultant, Pearl Meyer & Partners, to provide information on current developments and practices in director compensation.",
 {'entities': [(46, 68, 'CC')]})
,("Pearl Meyer & Partners is the same consultant retained by the Compensation Committee to advise on executive compensation, but performs no other work for ExxonMobil."
 , {'entities': [(0,22, 'CC')]})
,("The Committee considers factors that could affect Pearl Meyer & Partners’ independence, including that the consultant provides no other services for ExxonMobil other than its engagement by the Committee and the Board Affairs Committee as described above. Based on this review, the Committee has determined the consultant’s work for the Committee to be free from conflicts of interest."
 , {'entities': [(50,72, 'CC')]})
,("The committee retains its own independent consultant, Frederic W. Cook & Co. Inc., to provide additional analysis and advice. The Cook firm does not provide any services to the company except for the services it provides directly to the committee." 
 , {'entities':[(54,81,"CC"), (126,139,'CC')]})
,("In addition, the Compensation and Benefits Committee (the “Committee”) retains its own consultant, Frederic W. Cook of Frederic W. Cook & Company, to analyze market data and to provide general compensation advice to the Committee, particularly on CEO compensation. Mr. Cook and his firm do not provide any services to the company other than the services provided directly to the Committee."
 , {'entities':[(119,145, "CC")]})
,("The Compensation and Benefits Committee has authority to retain its own advisors, including compensation consultants."
  , {'entities': []})
,("In 2010, the Committee retained an independent compensation consultant, Frederic W. Cook & Co. who provided advice as requested by the committee, including, among other things, a review of the company’s compensation plans for executives, advice on setting the CEO’s compensation, comments on the CD&A for this proxy statement, and advice on changes in compensation practices and policies described in the CD&A."
  , {'entities':[(72,94,"CC")]})
, ("Frederic W. Cook & Co. does not provide any services to the company other than the services provided directly to the committee." 
  , {'entities':[(0,22,"CC")]})
, ("We use comparative compensation data from Towers Watson to help evaluate whether our compensation programs are competitive with the market. The comparative compensation data are not customized based on parameters developed by Towers Watson. Towers Watson does not provide any executive compensation advice to the Compensation and Benefits Committee."
  , {'entities': [(42,55,"CC"),(226,239,"CC"),(241,254,"CC")]})
, ("The Committee retained Frederic W. Cook & Co. for the first part of 2011 and Pay Governance LLC for the second part of the year."
   , {'entities':[(23,45,"CC"),(77,95,"CC")]})
, ("The Committee undertook a review of compensation consulting firms in 2011 as a matter of good corporate governance practices."
   , {'entities': []})
, ("As a result of that review, the Committee retained Pay Governance LLC in October."
   , {'entities': [(51,69,"CC")]})
, ("Both provided advice as requested by the Committee, including, among other things, review of the Company’s compensation plans for executives and advice on setting the CEO’s compensation."
   , {'entities': []}) 
, ("Pay Governance LLC provided advice on the CD&A in this proxy statement. Neither consultant provides any services to the Company other than the services provided directly to the Committee."
   , {'entities': [(0,18,"CC")]})
, ("We use comparative compensation data from Towers Watson to help evaluate whether our compensation programs are competitive with the market."
   , {'entities': [(42,55,"CC")]})
, ("The Governance and Nominating Committee reviews director compensation periodically and recommends changes to the Board, when it deems appropriate, based on market information provided to the committee by Pearl Meyer & Partners, an independent compensation consultant, and taking into account various factors, including the responsibilities of directors generally, the responsibilities of committee chairs, and Company performance."
   , {'entities':[(204,226,"CC")]})
, ("In 2012, the Committee directly retained Pay Governance LLC, which is independent and without conflicts of interest with the Company."
   , {'entities':[(41,59,"CC")]})
, ("Pay Governance LLC provided advice as requested by the Committee, on the amount and form of certain executive compensation components, including, among other things, executive compensation best practices, insights concerning SEC and say on pay policies, analysis and review of the Company’s compensation plans for executives and advice on setting the CEO’s compensation."
   , {'entities':[(0,18,"CC")]})
, ("Pay Governance LLC also provided advice on the Compensation Discussion and Analysis in this proxy statement."
   , {'entities':[(0,18,"CC")]})
, ("Pay Governance LLC did not provide any services to the Company other than the services provided directly to the Committee."
   , {'entities':[(0,18,"CC")]})
, ("Towers Watson does not provide any advice or recommendations to the Compensation and Benefits Committee on the amount or form of executive or director compensation."
   , {'entities':[(0,13,"CC")]})
, ("The comparative compensation data are not customized based on parameters developed by Towers Watson."
   , {'entities':[(86,99,"CC")]})
, ("During 2013, the Company continued to retain Pearl Meyer & Partners to provide consultation services regarding non-employee director compensation."
   , {'entities':[(45,67,"CC")]})
, ("We do not currently engage any consultant related to executive and/or director compensation matters."
   ,  {'entities': []})
, ("Regarding most compensation matters, including executive and director compensation and the Company's salary cap, Company management provides recommendations to the Compensation Committee."
   ,{'entities': []})
, ("The Company did not engage any consultant related to executive and/or director compensation reported for fiscal year 2008"
   , {'entities': []})
, ("Regarding most compensation matters, including executive and director compensation and the Company’s salary cap, the Company’s executive team provides recommendations to the Compensation Committee. The Company did not engage any consultant related to executive and/or director compensation reported for fiscal year 2009."
   , {'entities': []})
, ("In August 2005, the Compensation Committee retained Mercer Human Resources Consulting as its compensation consultant."
   , {'entities':[(52,85,"CC")]})
, ("The Compensation Committee’s relationship with Mercer is reviewed annually and has continued in fiscal 2007 with Mercer attending all meetings of the Compensation Committee held during the year."
   , {'entities':[(47,53,"CC"),(113,119,"CC")]})
, ("The Compensation Committee, with guidance from Mercer, determines the composition of our peer group and reevaluates this group on an annual basis. For fiscal 2007, our peer group consisted of 19 U.S.-based technology companies of comparable size and performance to us. Most of the companies included in our peer group are also included in the Dow Jones U.S. Technology, Hardware and Equipment Index. Below is a list of the companies in our peer group in fiscal 2007."
   , {'entities':[(47,53,"CC")]})
, ("As part of this review, the Committee’s compensation consultant, Mercer, reviews and evaluates the competitiveness of our director compensation program in light of general director compensation trends and director compensation programs of our peer group companies, which are listed in the “Compensation Discussion and Analysis” section below."
   , {'entities':[(65,71,"CC")]})
, ("The Compensation Committee’s relationship with Mercer is reviewed annually and has continued in fiscal 2008 with Mercer attending all in-person meetings of the Compensation Committee held during the year."
   , {'entities':[(47,53,"CC"),(113,119,"CC")]})
, ("The Compensation Committee’s practice has been to retain compensation consultants to provide objective advice and counsel to the Compensation Committee on all matters related to the compensation of executive officers and directors. For fiscal 2009, the Compensation Committee retained Mercer (US) Inc. (“Mercer”) as its compensation consultant, with Mercer attending all in-person meetings of the Compensation Committee held during the year."
   , {'entities':[(285,301,"CC"),(304,310,"CC"),(350,356,"CC")]})
,("Mercer’s role in the compensation-setting process includes providing recommendations regarding the composition of our peer group, gathering and analyzing proxy data for our peer group, analyzing pay survey data, providing best practices and advice regarding compensation trends, reviewing and advising on the performance measures used in bonus formulas, and reviewing and advising the Compensation Committee on management recommendations regarding compensation. Although Mercer communicates with management to gather information and review management recommendations, Mercer reports directly to the Compensation Committee."
  , {'entities':[(0,6,"CC"),(471,477,"CC"),(568,574,"CC")]})
,("For fiscal 2010, the Compensation Committee retained Mercer (US) Inc. (“Mercer”), a wholly owned subsidiary of Marsh & McLennan Companies, Inc. (“MMC”), as its compensation consultant, with Mercer attending all in-person meetings of the Compensation Committee held during the year."
  , {'entities':[(53,69,"CC"),(72,78,"CC"),(190,196,"CC")]})
,("Mercer’s fees for executive compensation consulting to the Committee in fiscal 2010 were approximately $247,000."
  , {'entities':[(0,6,"CC")]})
,("During fiscal 2010, certain MMC affiliates were retained by company management to provide services unrelated to executive compensation, including welfare plan consulting, actuarial and plan administration services with respect to the company’s general health and welfare benefit plans and programs."
  , {'entities': []})
,("Mercer and its affiliates have established and followed safeguards between the executive compensation consultants engaged by the Compensation Committee and the other MMC service providers to the company, which are designed to help ensure that the Compensation Committee’s executive compensation consultants continue to fulfill their role in providing objective, unbiased advice."
  , {'entities':[(0,6,"CC")]})
,("Our Compensation Committee reviews our non-employee director compensation on an annual basis. As part of this review, the Committee’s compensation consultant, Mercer, reviews and evaluates the competitiveness of our director compensation program in light of general director compensation trends and director compensation programs of our peer group companies, which are listed in the “Compensation Discussion and Analysis” section below."
  ,{'entities':[(159,165,"CC")]})
,("In making its determination with respect to executive compensation, the Compensation Committee has previously engaged the services of a compensation consultant.  In 2004, the Compensation Committee engaged Hewitt Associates LLC, a compensation consulting firm, to undertake a study of the Company’s compensation programs (the “Hewitt Study”).  Hewitt Associates assisted the Compensation Committee in redesigning the Company’s compensation programs and provided information with respect to executive compensation at companies with the same levels of revenues and earnings as the Company."
  ,{'entities':[(206,227,"CC"), (344,361,"CC")]})
, ("In the current 2007 fiscal year, the Compensation Committee consulted Exequity LLP for a general review in determining compensation for executive officers.  The Compensation Committee has the authority to retain, terminate and set the terms of the Company’s relationship with any outside advisors who assist the Committee in carrying out its responsibilities."
  , {'entities':[(70,82,"CC")]})
,("In connection with making its determinations for fiscal 2008, the Compensation Committee conducted a search for an independent compensation consultant and retained James F. Reda & Associates LLC (“JFR”) to conduct a compensation review for the named executive officers and certain other officers."
  ,{'entities':[(164,194,"CC"), (197,200,"CC")]})
, ("Based on the recommendations and data from James F. Reda & Associates LLC (“JFR”), the independent compensation consultant retained by the Compensation Committee, and other factors, and in light of the Company’s strong financial results for fiscal 2009, the Compensation Committee determined that the named executive officers of the Company should receive the total compensation packages for fiscal 2010, as further described below."
   , {'entities':[(43,73,"CC"), (76,79,"CC")]})
, ("The Compensation Committee has the authority to retain, terminate and set the terms of the Company’s relationship with any consultants and other outside advisors who assist the Compensation Committee in carrying out its responsibilities.  In connection with making its determinations regarding compensation for our named executive officers and certain other key executives for the fiscal year ended February 28, 2009 (“fiscal 2008”), the Compensation Committee conducted a search for an independent compensation consultant and retained JFR to conduct a compensation review for the named executive officers and certain other executives."
   , {'entities':[(536,539,"CC")]})
, ('JFR had not previously worked with the Company in any capacity and has not served the Company in any capacity, except as consultants to the Compensation Committee.  The Compensation Committee has continued to retain JFR for fiscal 2009, 2010 and 2011.'
   , {'entities':[(0,3,"CC"), (216,219,"CC")]})
, ('The Compensation Committee also receives advice and assistance from the law firm of Chadbourne & Parke LLP, which has acted as counsel only to the Company’s independent directors and its Board committees.'
   , {'entities': []})
, ('Based on the recommendations and data from James F. Reda & Associates, a division of Gallagher Benefit Services, Inc. (“JFR”), the independent compensation consultant retained by the Compensation Committee, and other factors, and in light of the Company’s strong financial results for fiscal 2011 (as described above), and the growth in the size and scope of the Company, the Compensation Committee determined that the named executive officers of the Company should receive the total compensation packages for fiscal 2012, as further described below.'
   , {'entities':[(43,69,"CC"), (85,117,"CC"), (120,123,"CC")]})
, ("Based on the recommendations and data from Arthur J. Gallagher & Co., formerly James F. Reda & Associates, a division of Gallagher Benefit Services, Inc. (“Gallagher”), the independent compensation consultant retained by the Compensation Committee, and other factors, and in light of the Company’s strong financial results for fiscal 2012 (as described above), and the growth in the size and scope of the Company, the Compensation Committee determined that the named executive officers of the Company should receive the total compensation packages for fiscal 2013, as further described below."
   , {'entities':[(43,68,"CC"), (79,105,"CC"), (121,153,"CC"), (156,165,"CC")]})
, ("In connection with making its determinations regarding executive compensation for fiscal 2014 and for several prior years, the Compensation Committee retained Arthur J. Gallagher & Co. Human Resources & Compensation Consulting Practice (“Gallagher”) or its predecessor to conduct a compensation review for the named executive officers and certain other executives.  Gallagher has not served the Company in any other capacity except as consultants to the Compensation Committee."
   , {'entities':[(159,235,"CC"), (238,247,"CC"), (366,375,"CC")]})
, ('The Compensation and the Nominating and Corporate Governance Committees also receive advice and assistance from the law firm of Chadbourne & Parke LLP, which has acted as counsel only to the Company’s independent directors and its Board committees.'
   , {'entities': []})
,("Under the direction of the Compensation Committee, the compensation review included a peer group competitive market review of executive compensation and total compensation recommendations by Gallagher."
  , {'entities':[(191,200,"CC")]})
,("The peer group developed by Gallagher, agreed upon by the Compensation Committee and upon which it based its recommendations for fiscal 2014 compensation, consisted of 19 retail companies of a size range based on revenue and net income relatively closely aligned with the Company’s revenue and net income, all of them in the retail industry."
  , {'entities':[(28,37,"CC")]})
, ("Effective in 2009, the Committee has engaged Frederic W. Cook & Co., Inc. to provide executive compensation consulting services. Frederic W. Cook & Co., Inc. does not provide any consulting services to Whirlpool and works exclusively with the Committee as an independent consultant."
   , {'entities':[(45,73,"CC"),(129,157,"CC")]})
,("Our Human Resources Committee establishes target compensation levels using a market-based approach. Each year, the Committee engages an independent compensation advisor to advise the Committee on Whirlpool’s executive compensation program. At the beginning of 2007, the Committee retained Hewitt Associates, an outside human resources consulting firm, as its independent executive compensation advisor to provide data and analysis regarding pay levels for our NEOs and other senior executives."
  , {'entities':[(289,306,"CC")]})
,("Specifically, the Committee requested that Hewitt Associates assist the Committee in (1) reviewing the group of companies against whom Whirlpool’s senior executive pay levels are compared (our “comparator group”); (2) reviewing executive compensation market practices and trends in general; (3) designing and recommending the compensation packages provided to the named executive officers (“NEOs”) and other senior executives; and (4) providing a marketplace assessment of the compensation for the NEOs and other senior executives in comparison to the compensation for comparable positions within the comparator group."
  , {'entities':[(43,60,"CC")]})
,("Other than the work it performs for the Committee, Hewitt Associates provides minimal compensation consulting services to Whirlpool such as providing market data for non-senior management compensation and actuarial services to Whirlpool’s European and Asian regions. Hewitt Associates has been the Committee’s compensation advisor since 2003 and was most recently reappointed in 2006.", 
  {'entities':[(51,68,"CC"),(267,284,"CC")]})
, ("The Committee periodically reviews other compensation consultants and the Committee Chair met with several consultants in the fourth quarter of 2008. Effective in 2009, the Committee has engaged Frederic W. Cook & Co., Inc. to provide executive compensation consulting services. Frederic W. Cook & Co., Inc. does not provide any consulting services to Whirlpool and works exclusively with the Committee as an independent consultant."
  , {'entities':[(195,223,"CC"),(279,307,"CC")]})
, ("The Committee establishes target compensation levels using a market-based approach. Each year, the Committee engages an independent compensation consultant to advise the Committee on Whirlpool’s executive compensation program. The Committee has the sole authority to approve the independent compensation consultant’s fees and terms of engagement."
  , {'entities': []})
, ("In setting long-term compensation, the Committee may give more weight to the complexity of the individual’s position and impact on overall company results. While the Committee solicits and reviews recommendations from its independent compensation consultant, and in some circumstances management, ultimately the Committee makes decisions regarding these matters in the exercise of its sole discretion."
  , {'entities': []})
, ("In 2009, the Committee selected Frederic W. Cook & Co. as its independent compensation consultant because of its extensive expertise and its independence due to the lack of an existing business relationship with Whirlpool."
   ,{'entities':[(32,54,"CC")]})
, ("Frederic W. Cook & Co. performed no services for Whirlpool in 2010 other than those related to executive and nonemployee director compensation as discussed below."
   , {'entities':[(0,22,"CC")]})
, ("Frederic W. Cook & Co. advised the Committee on the design of the 2010 Omnibus Stock and Incentive Plan and the executive compensation provisions of the Dodd-Frank Act."
   , {'entities':[(0,22,"CC")]})
, ("Frederic W. Cook & Co. also performed a comprehensive analysis of the company’s change in control severance agreements and assisted in the preparation of revised agreements as discussed below under “Post-termination Payments.” Frederic W. Cook & Co. also assisted the Committee with a variety of other ongoing items, including review of materials prepared by management in advance of Committee meetings, the design of the variable incentive plans and selection of performance metrics and the review of public disclosures including this CD&A and the accompanying tables and narrative footnotes."
   , {'entities':[(0,22,"CC"),(227,249,"CC")]})
, ("As part of its ongoing role in supporting the Committee, Frederic W. Cook & Co. assists the Committee in (1) reviewing the group of companies against whom Whirlpool’s senior executive pay levels are compared (our “comparator group”); (2) reviewing executive compensation market practices and trends in general; and (3) designing and recommending the compensation packages provided to the NEOs and other senior executives based on a marketplace assessment of the compensation for the NEOs and other senior executives in comparison to the compensation for comparable positions within the comparator group."
   , {'entities':[(57,79,"CC")]})
, ("With respect to the CEO, Frederic W. Cook & Co. provides a recommendation, without the CEO’s input, to the Committee regarding the CEO’s compensation package (base salary, target incentive award levels and mix of pay components)."
   , {'entities':[(25,47,"CC")]})
, ("Each year, the CEO and Chief Human Resources Officer make recommendations to the Committee regarding the compensation and benefit programs for all executive officers." 
   , {'entities': []})
, ("In addition to the work described above, Frederic W. Cook & Co. also prepared a competitive assessment and report on the design of the company’s nonemployee director compensation program. Because decisions related to potential changes to nonemployee director compensation are made by the full Board of Directors, Frederic W. Cook & Co. provided its analysis to the Corporate Governance and Nominating Committee who then made a recommendation to the full Board."
   , {'entities':[(41,63,"CC"),(313,335,"CC")]})
, ("In making its determinations, the Committee reviews and considers various factors and assigns different weightings to these factors depending on the type of determination and the circumstances related to each specific action. For example, in determining base salary, the Committee may rely more heavily on market data and the guidance of its independent compensation consultant. In determining the payout of incentive awards, the Committee’s consideration of company performance and management’s assessment of individual performance may predominate. In setting long-term compensation, the Committee may give more weight to the complexity of the individual’s position and impact on overall company results. While the Committee solicits and reviews recommendations from its independent compensation consultant, and in some circumstances management, ultimately the Committee makes decisions regarding these matters in the exercise of its sole discretion."
   , {'entities': []})
, ("In addition, the CEO makes recommendations with respect to base salary, annual cash incentives, equity compensation, and the total compensation levels for executive officers other than himself based on his assessment of personal performance and contribution to Whirlpool."
   , {'entities': []})
, ("The CEO and Chief Human Resources Officer recommend the performance metrics to be used in establishing performance goals for the annual cash incentive and long-term equity and cash incentive programs for adoption by the Committee."
   , {'entities': []})
, ("The Committee has authority to adopt or modify these metrics in its sole discretion. In addition, the CEO assesses the individual performance of the executive officers to assist the Committee in making determinations regarding awards to be paid out under incentive programs."
   , {'entities': []})
, ("The Committee retains the services of an outside consultant to assist it in performing its duties (the HRC Consultant)."
   , {'entities':[(99,117,"CC")]})
, ("The HRC Consultant is engaged by, and reports directly to, the Committee."
   , {'entities':[(0,18,"CC")]})
, ("The HRC Consultant generally attends all meetings of the Committee. Following each Committee meeting, the Committee reports to the Board of Directors on its actions and recommendations and the Committee periodically meets in executive session without members of management present."
  , {'entities':[(0,18,"CC")]})
, ("Although the Committee receives recommendations from the Executive Vice President of Human Resources and from the HRC Consultant regarding the design and level of compensation to be provided to Verizon’s named executive officers, the Committee ultimately makes all final decisions as to the compensation levels for these executives."
   , {'entities':[(110,128,"CC")]})
, ("The Committee believes that an appropriate level of input from management and input from the HRC Consultant provide a necessary and valuable perspective in helping the Committee formulate its own independent views on compensation."
   , {'entities':[(89,107,"CC")]})
, ("With the assistance of the HRC Consultant, the Committee annually compares Verizon’s total direct compensation and component pay levels to those of its market and industry peer group companies in order to ensure competitiveness."
   , {'entities':[(23,41,"CC")]})
, ("In recognition of the ongoing transformation of the Company’s business, Mr. Seidenberg and the Committee, in consultation with the HRC Consultant, reviewed the current market conditions and discussed the competitive assessment of the amount and terms of Mr. Seidenberg’s long-term incentive award."
   , {'entities':[(127,145,"CC")]})
, ("In 2006 the Committee retained Pearl Meyer and Partners to act as its independent compensation consultant."
   , {'entities':[(31,55,"CC")]})
, ("Pearl Meyer does not perform any services for the Company other than those provided to the Committee."
   , {'entities':[(0,11,"CC")]} )
, ("In August 2006, after a thorough evaluation, the Committee retained Pearl Meyer & Partners to act as its independent outside compensation consultant, replacing Hewitt Associates LLP, which had served as the Committee’s compensation consultant since 2000."
   , {'entities':[(68,90,"CC"),(160,181,"CC")]})   
, ("Separately, Hewitt provides employee benefits administration and actuarial services to the Company on behalf of its active and retiree management and union employees."
   , {'entities':[(12,18,"CC")]})
, ("Pearl Meyer & Partners does not provide any services to the Company other than those provided to the Committee."
   , {'entities':[(0,22,"CC")]})
, ("The Committee has the authority to retain and terminate a compensation consultant and approves the consultant’s fees, assignments and other terms of its engagement."
   ,{'entities': []})
, ("The compensation consultant is referred to throughout this discussion and analysis as the Consultant."
   , {'entities': []})
, ("The Committee has retained Pearl Meyer & Partners to act as its independent compensation consultant."
   , {'entities':[(27,49,"CC")]})
, ("In the discussion and analysis of compensation we refer to the compensation consultant as the Consultant."
   ,{'entities': []})
, ("In compliance with the terms of this policy, Pearl Meyer & Partners has not performed any work for the Company since the date it was retained by the Committee."
   , {'entities':[(45,67,"CC")]})
, ("If the executive is dead, you’re certainly not retaining them,” said Steven Hall, a compensation consultant."
   , {'entities':[(69,80,"CC")]})
, ("The Committee has retained Pearl Meyer & Partners as its consultant (the 'Consultant')"
   , {'entities':[(27,49,"CC")]})
, ("In compliance with the terms of this policy, neither Pearl Meyer & Partners nor its affiliates have performed any work for the Company or any Company affiliate since the date it was retained by the Committee in 2006."
   , {'entities':[(53,75,"CC")]})
, ("At the request of the Committee, management and the Committee’s compensation consultant, Pearl Meyer & Partners (the “Consultant”), engage in a semiannual shareholder outreach program with certain institutional investors to discuss the design and operation of Verizon’s executive compensation program."
   , {'entities':[(89,111,"CC")]})
, ("The Committee requested and received a letter from Pearl Meyer & Partners addressing the consulting firm’s independence, including the following factors: (1) other services provided to the Company by the consulting firm; (2) fees paid by the Committee as a percentage of the consulting firm’s total revenue; (3) policies or procedures maintained by the consulting firm that are designed to prevent a conflict of interest; (4) any business or personal relationships between the individual consultants involved in the engagement and a member of the Committee; (5) any Company stock owned by the individual consultants involved in the engagement; and (6) any business or personal relationships between our executive officers and the consulting firm or the individual consultants involved in the engagement."
   ,{'entities':[(51,73,"CC")]})
, ("The Committee has considered the independence of Pearl Meyer & Partners in light of new SEC rules and NYSE and Nasdaq listing standards."
   , {'entities':[(49,71,"CC")]})
, ("The Committee has retained Pearl Meyer & Partners as its compensation consultant (Consultant) based on its experience representing large corporations and its independence."
   , {'entities':[(27,49,"CC")]})
, ("In fiscal 2014, the Board and Compensation Committee reviewed competitive market data compiled by Compensia, Inc., the Compensation Committee’s independent compensation consultant (“Compensia”)."
   , {'entities':[(98,107,"CC"),(182,191,"CC")]})
, ('The Committee has engaged Frederic W. Cook & Co., Inc. (“F.W. Cook”) to act as its compensation consultant.'
   , {'entities':[(26,54,"CC"),(57,67,"CC")]})
, ("F.W. Cook’s sole engagement for the Company is as compensation consultant to the Committee."
   , {'entities':[(0,9,"CC")]})    
, ("In 2006 the Compensation Committee engaged SMG Advisory Group LLC, or SMG, a nationally recognized consulting firm specializing in the real estate industry, to assist the committee in determining the amount and form of executive compensation and considered information presented by Mercer Human Resource Consulting, or Mercer, an independent compensation consultant, when reviewing the appropriate types and levels for the Company’s non-employee director compensation program."
   , {'entities':[(43,65,"CC"),(70,73,"CC"),(282,314,"CC"),(319,325,"CC")]})
, ("In 2007 the Compensation Committee again retained SMG Advisory Group LLC (“SMG”), a nationally recognized consulting firm specializing in the real estate industry that was first engaged in the fourth quarter of 2006. "
   , {'entities':[(50,72,"CC"),(75,78,"CC")]})
, ("Neither the Compensation Committee nor the Company has any other professional relationship with SMG."
   , {'entities':[(96,99,"CC")]})
, ("The Compensation Committee directed SMG to, among other things: (1) assist the Compensation Committee in applying our compensation philosophy for our executive officers, including the determination of the portion of total compensation awarded in the form of salary, cash bonus and equity-based compensation, and, for the latter, allocating between time-based and performance-based vesting, as well as selecting the appropriate performance metrics and levels of performance"
   , {'entities':[(36,39,"CC")]})
, ("In 2007 SMG conducted a peer group analysis similar to the one they conducted in 2006."
   , {'entities':[(8,11,"CC")]})
, ("SMG’s review compared our executive pay practices against both an expanded REIT peer group and a selective office REIT peer group to determine the range of cash and equity-based compensation awarded to executives in comparable positions to our executives in terms of base salary, annual bonus and annual long-term compensation awards."
   , {'entities':[(0,3,"CC")]})
, ("SMG also analyzed outperformance compensation (both in terms of outperformance rewards realized and potential rewards for those awards that have not yet been realized), but did not include outperformance awards in its overall annual compensation analysis for peer companies that grant them, because until 2008 we did not have an outperformance program."
   , {'entities':[(0,3,"CC")]})
, ("The Compensation Committee with assistance from SMG reviewed this information, including statistical analysis and a comparison of the roles and responsibilities of individual executives at the Company and at the various peer companies."
   , {'entities':[(48,51,"CC")]})
, ("The Compensation Committee received from SMG detailed information regarding equity ownership value and dividend income relative to total compensation for chairmen and chief executive officers within the combined peer groups, as compared to those for Messrs. Zuckerman and E. Linde."
   , {'entities':[(41,44,"CC")]})
, ("Ms. Baird had served as Counselor and Staff Executive of General Electric Co., a partner in the international law firm of O’Melveny and Myers, an associate general counsel to President Jimmy Carter and an attorney in the Office of Legal Counsel of the United States Department of Justice."
   , {'entities': []})
, ("SMG advised the Compensation Committee that both the expanded peer group and the selective office sector peer group generally have compensation programs comparable to ours, with annual bonuses generally in the form of cash ranging between 150% and 250% of base salary and annual long-term compensation generally in the form of equity with time-based vesting over three to five years."
   , {'entities':[(0,3,"CC")]})
, ("In 2008 the Compensation Committee again retained The Schonbraun McCann Group, a real estate advisory practice of FTI Consulting, Inc. (“SMG”), a nationally recognized consulting firm specializing in the real estate industry that was first engaged in the fourth quarter of 2006. Neither the Compensation Committee nor the Company has any other professional relationship with SMG."
   , {'entities':[(50,77,"CC"),(137,140,"CC")]})
, ('In accordance with this policy, in the fall of 2008, the Company engaged Mercer Human Resource Consulting, an independent compensation consultant, to assist it in conducting a competitive review of the Company’s non-employee director compensation program.'
   , {'entities':[(73,105,"CC")]})
, ("In 2011, the Compensation Committee engaged FTI Consulting, Inc. (“FTI”) and in 2012 the Compensation Committee engaged FPL Associates L.P. (“FPL”), to assist the committee in determining the amount and form of executive compensation."
   , {'entities':[(44,64,"CC"),(67,70,"CC"),(120,139,"CC"),(142,145,"CC")]})
, ("The Compensation Committee retained FPL as its advisor in November 2012 and during 2013 assessed and affirmed the independence of FPL in connection with renewal of the engagement."
   , {'entities':[(36,39,"CC"),(130,133,"CC")]})
, ("The Compensation Committee has retained FPL as its advisor since 2012 and every year re-assesses and re-affirms the independence of FPL in connection with renewal of the engagement."
   , {'entities':[(40,43,"CC"),(132,135,"CC")]})
, ("In addition to the assistance provided by Biogen Idec’s internal Compensation and Benefits group, the Committee currently engages Frederic W. Cook & Co., Inc (Cook) as an independent compensation consultant."
   , {'entities':[(130,157,"CC"),(159,163,"CC")]})
, ("Cook replaced Watson Wyatt Worldwide (Watson Wyatt) in this role in July 2009."
   , {'entities':[(0,4,"CC"),(14,36,"CC"), ((38,50,"CC"))]})
, ("Cook reports directly to the Committee to provide guidance on matters including trends in executive and non-employee director compensation, the development of specific executive compensation programs, the composition of the Company’s compensation peer group and other matters as directed by the Committee"
   , {'entities':[(0,4,"CC")]})
, ("Cook does not provide any other services to Biogen Idec."
   , {'entities':[(0,4,"CC")]})    
, ("The Committee believes that independent advice is important in developing Biogen Idec’s executive compensation program and currently engages Frederic W. Cook & Co., Inc. (Cook) as its independent compensation consultant."
   , {'entities':[(141,169,"CC"),(171,175,"CC")]})
,("The Committee assessed Cook’s independence in December 2012 in accordance with the principles set forth in its Charter and confirmed that the firm’s work has not raised any conflict of interest and that the firm is independent under the terms of its Charter."
  , {'entities':[(23,27,"CC")]})
, ("Frederic W. Cook & Co., Inc. (FWC) is currently engaged as the Compensation Committee’s independent compensation consultant."
   , {'entities':[(0,28,"CC"),(30,33,"CC")]})
, ("Additionally, FWC prepares a report on CEO pay that compares each element of compensation to executives in comparable positions at companies in our peer group."
   , {'entities':[(14,17,"CC")]})
, ("FWC also engages in other matters as needed and as directed solely by the Compensation Committee."
   , {'entities':[(0,3,"CC")]})
, ("The committee has retained the services of Hay Group, an independent compensation consultant, in order to obtain access to independent compensation data, analysis and advice."
   , {'entities':[(43,52,"CC")]})
, ("Hay Group was initially engaged by the committee in November 2005 and presented a comprehensive executive compensation review to the committee in January 2006."
   , {'entities':[(0,9,"CC")]})
, ("In December 2008, the committee retained the services of Frederic W. Cook & Co., Inc. (“Cook & Co.”), an independent compensation consultant, to assist the committee in the review and evaluation of the company’s equity compensation practices. This review and evaluation did not have an effect on fiscal 2009 compensation, but will likely affect fiscal 2010 compensation, which we plan to discuss in our 2010 proxy statement. Cook & Co. provides no other services to the company."
   , {'entities':[(57,85,"CC"),(88,98,"CC"), (425,435,"CC")]})
, ("The committee has retained the services of Hay Group, an independent compensation consultant, in order to obtain access to independent compensation data, analysis and advice. Hay Group was initially engaged by the committee in November 2005 and, from time to time, has presented comprehensive executive compensation reviews to the committee. These presentations generally included a comparison of our executive compensation program with programs used by a peer group of companies as well as a discussion of broader market compensation trends, including market practices with respect to base salaries, annual bonuses and long-term incentive compensation. Hay Group provides no other services to the company."
   , {'entities':[(43,52,"CC"),(175,184,"CC"), (654,663,"CC")]})
, ("In fiscal 2013, the Committee engaged Frederic W. Cook & Co., Inc. (“FWC”), a compensation consultant, to obtain access to independent compensation data, analysis and advice."
   ,{'entities':[(38,66,"CC"),(69,72,"CC")]})
, ('The Committee chose FWC based on FWC’s expertise in executive compensation and FWC’s prior service as an advisor to the Committee in connection with the Company’s equity program.',
  {'entities': [(20, 23, 'CC'), (33, 36, 'CC'), (79, 82, 'CC')]})
, ("In fiscal 2013, the Committee engaged Frederic W. Cook & Co., Inc. (“FWC”), a compensation consultant, to obtain access to independent compensation data, analysis and advice. The Committee chose FWC based on FWC’s expertise in executive compensation and FWC’s prior service as an advisor to the Committee in connection with the Company’s equity program. Pursuant to its charter, the Committee has the sole authority to hire, oversee and terminate FWC, as well as to approve FWC’s fees and any other terms of the engagement. Committee members have direct access to FWC without going through management. FWC provides no services to CarMax other than those it provides to the Committee."
   , {'entities':[(38,66,"CC"),(69,72,"CC"),(195,198,"CC"),(208,211,"CC"),(254,257,"CC"),(474,477,"CC"), (564,567,"CC"), (602,605,"CC") ]})
, ('Pursuant to its charter, the Committee has the sole authority to hire, oversee and terminate FWC, as well as to approve FWC’s fees and any other terms of the engagement.'
   , {'entities':[(93, 96, 'CC'), (120, 123, 'CC')]})
, ('Compensation Committee members have direct access to FWC without going through management.'
   , {'entities': [(53, 56, 'CC')]})
, ('FWC provides no services to CarMax other than those it provides to the Committee.'
   , {'entities': [(0, 3, 'CC')]})
, ("In furtherance of these goals, the committee has retained Independent Compensation Committee Adviser, LLC, to provide independent evaluations and advice regarding executive compensation. The independent consultant reports directly to the chair of the committee and meets with the committee in executive session, without the presence of management. The committee also relies on Mercer Human Resource Consulting to provide data, evaluations and advice regarding executive compensation."
   , {'entities': [(58, 105, 'CC'), (377,409,"CC")]})
, ("The committee has retained Independent Compensation Committee Adviser, LLC to provide the committee with comparative data on executive compensation and advice on Citi’s compensation programs for senior management. Independent Compensation Committee Adviser, LLC does no other work for Citi. Citi has retained Mercer Human Resource Consulting for benchmarking and analyses with respect to executive compensation and benefit practices, and other compensation matters for all employees, including the named executive officers. The committee relies on information and analysis received from both compensation consultants."
   , {'entities': [(27, 74, 'CC'), (309,341,"CC")]})
, ("The committee has retained Independent Compensation Committee Adviser, LLC (icca) to provide the committee with comparative data on executive compensation and advice on Citi’s compensation programs for senior management. icca does no other work for Citi. The amount the personnel and compensation committee approved for payment to icca in 2008 is disclosed in the cd&a on page 50 of this proxy statement."
   , {'entities': [(27, 74, 'CC'), (221,225,"CC"), (331,335, "CC")]})
, ("The committee also has the authority to retain and/or engage special consultants or experts to advise the committee, as the committee may deem appropriate or necessary in its sole discretion, and receives funding from Citi to engage such advisors. The committee has retained Independent Compensation Committee Adviser, L.L.C. (ICCA) to provide the committee with advice on Citi’s compensation programs for senior management. ICCA reports solely to the committee and the committee has sole authority to retain, terminate, and approve the fees of ICCA. ICCA does no other work for Citi."
   , {'entities': [(275, 325, 'CC'), (327,331,"CC"), (425,429, "CC"), (545,549, "CC"), (551,555, "CC")]})
, ("The amount paid to ICCA in 2010 is disclosed in the CD&A on page 60 of this proxy statement. For 2010, no other compensation consultant has been engaged by the personnel and compensation committee."
   , {'entities': [(19,23, 'CC')]})
, ("The board has determined that in addition to being independent according to the board’s independence standards as set out in its Corporate Governance Guidelines, each of the members of the personnel and compensation committee is independent according to the corporate governance rules of the NYSE. Each of such directors is a “non-employee director,” as defined in Section 16 of the Securities Exchange Act of 1934, and is an “outside director,” as defined by Section 162(m) of the IRC."
   , {'entities': []})
, ("For the 2010 compensation year, the only consultant retained by the committee to advise the committee on its compensation determinations was Independent Compensation Committee Adviser, LLC (ICCA). ICCA has advised the committee since 2006 and has never performed work for Citi other than its assignments from the committee."
   , {'entities': [(141, 188, 'CC'), (190,194,"CC"), (197,201, "CC")]})
, ("During 2010, with the committee’s oversight and review, the CRO and management employed a tool developed by a third party consultant (Towers Watson) with input from Citi to identify and manage risks in incentive compensation plans."
   , {'entities': [(134,147, 'CC')]})
, ("The committee retained ICCA starting in 2006 as part of its effort to ensure the independence of the advice it receives. ICCA advises the committee on its compensation decisions regarding executive compensation and other compensation matters as requested by the committee."
   , {'entities': [(23, 27, 'CC'), (121,125,"CC")]})
, ("The Board has nominated all of the current Directors for re-election at the 2016 Annual Meeting. Each of the Director nominees that currently served on the Board was elected by the stockholders at the 2015 Annual Meeting of Stockholders, except for Ms. Costello, Ms. James and Mr. McQuade, who were previously elected by the Board in 2015. Mses. Costello and James were identiﬁed as potential Directors by Egon Zehnder, the Board’s nominating consultant. Mr. McQuade was recommended as a candidate for election to the Citigroup Board by his fellow directors on the Citibank Board, all of whom are members of Citigroup’s Board. If elected, each nominee will hold ofﬁce until the 2017 Annual Meeting or until his or her successor is elected and qualiﬁed."
   , {'entities': []})
, ("Cook & Co. reports directly to, and is directly accountable to, the Compensation Committee. The Compensation Committee has the sole authority to retain, terminate, and obtain the advice of Cook & Co. at Citi’s expense."
   , {'entities': [(0, 10, 'CC'), (189,199,"CC")]})
, ("The Compensation Committee conducts a formal assessment of the independence of Cook & Co. at least annually. In performing the annual assessment of compensation advisor independence, the Compensation Committee considers various factors bearing on advisor independence, including the nature and amount of work performed for the Compensation Committee during the year, the nature of any unrelated services performed for Citi, the amount of fees paid for those services in relation to the ﬁrm’s total revenues, the advisor’s policies and procedures designed to prevent conﬂicts of interest, and the existence of any business or personal relationship that could impact the advisor’s independence."
   , {'entities': [(79,89, 'CC')]})
, ("The Committee has retained Frederic W. Cook & Co. (Cook & Co.) to provide the Committee with advice on Citi’s compensation programs for senior management. The amount paid to Cook & Co. in 2014 is disclosed in the Compensation Discussion and Analysis on page 69 of this Proxy Statement."
   , {'entities': [(27, 49, 'CC'), (51,61,"CC"), (174,184,"CC")]})
, ("The Committee has the power to hire and fire independent compensation consultants, legal counsel, or financial or other advisors (each, a “Compensation Advisor”) as it may deem necessary to assist it in the performance of its duties and responsibilities, without consulting or obtaining the approval of senior management of the Company. The Committee has retained Frederic W. Cook & Co. (Cook & Co.) to provide the Committee with advice on Citi’s compensation programs for senior management. The amount paid to Cook & Co. in 2013 is disclosed in the Compensation Discussion and Analysis on page 69 of this Proxy Statement."
   , {'entities': [(364, 386, 'CC'), (388,398,"CC"), (511,521,"CC")]})
, ("In 2005, the Committee engaged Mercer Human Resources Consulting to independently review Motorola’s Senior Leadership Team compensation. This study found that Motorola’s current executive compensation programs are fundamentally competitive and sound. The Committee agreed with the Mercer study’s conclusions that no substantive revisions to the compensation programs are required."
   , {'entities': [(31,64,'CC'), (281,287,"CC")]})
, ("In accordance with this authority, in 2007 and 2008, the Compensation and Leadership Committee retained Mercer (“Mercer”) as an external independent consultant to provide insight and advice on matters regarding trends in executive compensation, relative executive pay and benefits practices, relative assessment of pay of Motorola executives to performance, and other topics as the Compensation and Leadership Committee deemed appropriate."
   , {'entities': [(104,110,'CC'), (113,119,"CC")]})
, ("In its 2007 and 2008 independent reviews of Motorola’s senior leadership team’s compensation, Mercer found that Motorola’s current executive compensation programs are fundamentally competitive and sound."
   , {'entities': [(94,100,'CC')]})
, ("In 2007, the Compensation and Leadership Committee engaged Mercer to assist the Committee in its review of the compensation for Motorola’s non-employee directors."
   , {'entities': [(59,65,'CC')]})
, ("The Compensation and Leadership Committee agreed with the Mercer studies’ conclusions that no substantive revisions to the compensation programs are required."
   , {'entities': [(58,64,'CC')]})
, ("Based upon the markets in which we compete for executive talent within our industries, the Committee approved our comparator group, and Mercer, the Committee’s independent consultant, confirmed that the companies comprising the comparator group were appropriate."
   , {'entities': [(136,142,'CC')]})
, ("The Global Long Term Incentive Practices Survey, published by Buck Consultants, an ACS company. Because these surveys contain competitive compensation market data on a number of companies spanning a number of different industries, our market analysis involves narrowing the available data to “cuts” that most accurately reflect our competitive labor market. We complete regression analyses using the appropriate “data cuts” to capture the most accurate market data possible."
   , {'entities': []})
, ("Dr. Jha’s employment agreement was approved by the Board, based in part on the recommendation of the Committee and other Board members involved in Dr. Jha’s hiring process. The Board members involved hired their own external CEO compensation advisor who, together with Mercer, the Committee’s consultant, and management developed the compensation package that is reflected in Dr. Jha’s employment agreement."
   , {'entities': [(269,275,'CC')]})
, ("Participants may consist of all employees of Motorola and its Subsidiaries and all non-employee directors of Motorola; provided, however, the following individuals shall be excluded from participation in the plan: (a) contract labor (including without limitation black badges, brown badges, contractors, consultants, contract employees and job shoppers) regardless of length of service; (b) employees whose base wage or base salary is not processed for payment by a Payroll Department of Motorola or any Subsidiary; (c) any individual performing services under an independent contractor or consultant agreement, a purchase order, a supplier agreement or any other agreement that the Company enters into for service. Any corporation or other entity in which a 50% or greater interest is at the time directly or indirectly owned by Motorola and which Motorola consolidates for financial reporting purposes shall be a “Subsidiary” for purposes of the Plan."
   , {'entities': []})
, ("he Global Rewards department in Motorola’s Human Resources organization supports the Compensation and Leadership Committee in its work and, in some cases, acts pursuant to delegated authority from the Compensation and Leadership Committee to fulfill various functions in administering Motorola’s compensation programs."
   , {'entities': []})
, ("n carrying out its duties, the Compensation and Leadership Committee has direct access to outside advisors, independent compensation consultants and others to assist them. During 2008 and 2009, the Compensation and Leadership Committee directly engaged an outside compensation consulting firm to assist them in their review of the compensation for Motorola’s executive officers."
   , {'entities': []})
, ("In September 2009, the Committee unilaterally chose to change its compensation consultant firm from Mercer to Compensation Advisory Partners LLC, retaining the same individual consultants formerly at Mercer."
   , {'entities': [(100, 106, 'CC'), (110,144,"CC"), (200,206,"CC")]})
, ('In accordance with this authority, in 2008 and 2009, the Compensation and Leadership Committee retained Mercer ("Mercer") and beginning in September 2009 changed its consultant firm to Compensation Advisory Partners LLC ("Compensation Advisory Partners").'
   , {'entities': [(104, 110, 'CC'), (113,119,"CC"), (185,219,"CC"), (222,252,"CC")]})
, ("The Global Rewards department in Motorola's Human Resources organization, together with the Senior Vice President, Human Resources and the Committee's independent compensation consultant, prepares recommendations regarding Co-CEO compensation and brings those recommendations to the Compensation and Leadership Committee."
   , {'entities': []})
, ('The non-employee director compensation package was recommended by Compensia, Inc. (“Compensia”), our Board’s independent compensation consultant.'
   , {'entities': [(66,81, 'CC'), (84,93,"CC")]})
, ("In accordance with this authority, in mid-2010, our Former Parent’s Compensation and Leadership Committee retained Compensia to provide independent compensation services to Motorola Mobility."
   , {'entities': [(115,124,'CC')]})
, ("Compensia provided insight and advice on matters regarding trends in executive compensation, relative executive pay and benefits practices, relative assessment of pay to performance of our executives, and may cover other topics as the Compensation and Leadership Committee deems appropriate."
   , {'entities': [(0,9,'CC')]})
, ("The Global Compensation department in Motorola Mobility’s Human Resources organization, the Senior Vice President, Chief People Officer and the Committee’s independent compensation consultant together prepare recommendations regarding Chairman and CEO compensation and brings those recommendations to our Compensation and Leadership Committee. The Chairman and CEO is not involved in the preparation of recommendations related to his compensation and does not participate in the discussions regarding his compensation at Committee meetings. The consultant is also available at such meetings."
   , {'entities': []})
, ("During 2010, the Former Parent Compensation Committee chose to continue the engagement of Compensation Advisory Partners, LLC as its independent compensation consultant."
   , {'entities': [(90,125,'CC')]})
, ('Prior to the Separation, the Former Parent Compensation Committee decided to engage another compensation consultant, Compensia as the compensation consultant to our Compensation Committee for Motorola Mobility compensation matters.'
   , {'entities': [(117,126,'CC')]})
, ("Our Compensation Committee has only engaged Compensia as its independent consultant and does not use Deloitte."
   ,{'entities': [(44,53, 'CC'), (101,109,"CC")]})
, ("During this period Mr. Bratton also served as a Senior Consultant to Kroll’s Public Services Safety Group and Crisis and Consulting Management Group. Mr. Bratton is currently the Vice Chairman of the Homeland Security Advisory Council. Mr. Bratton holds a Bachelor of Science degree from Boston State College, is a graduate of the FBI National Executive Institute, and the Senior Executive Fellows Program at Harvard’s John F. Kennedy School of Government."
   , {'entities': []})
, ('Since 2009, the committee has retained Compensation Advisory Partners, LLC (“Compensation Advisory Partners”) as its independent compensation consultant. During 2010, the Committee also engaged Deloitte Consulting LLP and Compensia on specific compensation matters.'
   , {'entities': [(39,74, 'CC'), (77,107,"CC"),(194,217, 'CC'), (222,231,"CC")]})
, ('In 2010, the Compensation and Leadership Committee also engaged Compensia as its consultant on Motorola Mobility compensation matters and engaged Deloitte Consulting LLP (“Deloitte Consulting”) on Co-CEO employment agreement matters.'
   , {'entities': [(64,73, 'CC'), (146,169,"CC"),(172,191, 'CC')]})
, ('The Committee engages an independent consultant, Compensation Advisory Partners LLC (“CAP”), to advise on the Company’s executive compensation strategy and program design and to provide regulatory and market trend updates. CAP carries out compensation reviews as directed by the Committee and provides recommendations on specific compensation for our CEO and input on specific compensation recommendations for our other executive officers.'
   , {'entities': [(49,83, 'CC'), (86,89,"CC"),(223,226, 'CC')]})
, ('In addition to utilizing the experience and knowledge of the Human Resources Committee and the Company’s Human Resources staff, the Human Resources Committee retains the services of an independent human resources consultant (the “Consultant”) in making its executive compensation decisions. Each year, the Company’s Human Resources staff selects several executive or other officer positions for benchmarking against comparable companies. The Consultant analyzes compensation data for the Chief Executive Officer and the named executive officers, as well as selected other executives, at comparable companies and prepares a written analysis (collectively, the “Independent Compensation Analysis”).'
   , {'entities': []})
, ('Executive base salaries are reviewed annually. In February 2005, the Human Resources Committee, on the recommendation of the Consultant, discussed Mr. Bleustein’s compensation and, based upon his planned retirement on April 30, 2005, the Human Resources Committee did not increase Mr. Bleustein’s salary or grant stock options or restricted stock to Mr. Bleustein. In April 2005, the Human Resources Committee discussed compensation for Mr. Ziemer who was expected to be elected the Company’s Chief Executive Officer and President effective as of the conclusion of the Company’s 2005 annual meeting of shareholders. After reviewing the information presented by and the recommendation of the Consultant, the Human Resources Committee approved a base salary for Mr. Ziemer of $750,000.'
   , {'entities': []})
, ('The Human Resources Committee is also responsible for reviewing the annual performance of the CEO with input from the independent directors of the Board who comprise the Nominating and Corporate Governance Committee (the “Nominating Committee”). Based upon the review of the annual performance of the CEO and competitive market data, the Human Resources Committee develops a compensation package for the CEO and recommends the CEO’s compensation package to the Nominating Committee for approval.'
   , {'entities': []})
, ('A consultant, Mercer Human Resource Consulting, provides external market compensation data to the Human Resources Committee. The committee evaluates the performance of the CEO and the external market compensation data to formulate the CEO’s salary and recommends such compensation for approval by the Nominating Committee.'
   , {'entities': [(14,46,'CC')]})
, ('The Nominating Committee is responsible for establishing, reviewing and revising compensation we pay to our directors. All members of the Nominating Committee are independent in accordance with the requirements of the New York Stock Exchange rules. The Nominating Committee, working with management and third party compensation consultants and reviewing benchmarked data from a comparator group of companies, determines director compensation that it believes is competitive with these companies. The Director Compensation Policy, generally with the aid of a compensation consultant, is reviewed periodically and when necessary revised. This policy was most recently revised in December 2006 to formally establish compensation for the Chairman of the Board and to provide for directors’ use of a motorcycle where doing so may further a company business objective.'
   , {'entities': []})
, ('Also, with the assistance of Mercer, the HR Committee looks to a group of comparator companies which it believes to be similar to Harley-Davidson in business characteristics and economics. These companies generally have similar characteristics, such as having a focus on manufacturing, engineering, lifestyle and strong product brands. In 2006, these 14 companies were as follows: Apple Inc., The Black & Decker Corporation, Brunswick Corporation, Eastman Kodak Company, Energizer Holdings, Inc., Fortune Brands, Inc., Hasbro, Inc., Mattel, Inc., Maytag Corporation, Polaris Industries, Inc., Snap-on Incorporated, The Stanley Works, Thor Industries, Inc., Whirlpool Corporation, and Xerox Corporation. The HR Committee reviews this comparator group periodically, and Mercer compiles data on compensation levels and reward practices from these comparator companies’ proxy disclosures.'
   , {'entities': [(29,35, 'CC'), (768,774,"CC")]})
, ('In 2006, the HR Committee retained the services of Mercer as its primary advisor on issues related to the HR Committee’s responsibilities.'
   , {'entities': [(51,57,'CC')]})
, ('In addition to the executive compensation work that Mercer performed for the HR Committee for 2006, management periodically engages Mercer to provide advice on other Human Resources issues, including reward strategy and incentive design, competitiveness of compensation programs and group benefits plans.'
   , {'entities': [(52,58, 'CC'), (132,138,"CC")]})
, ('For the majority of 2007, the Human Resources Committee retained the services of Mercer as its outside executive compensation advisor on issues related to the Human Resources Committee’s responsibilities. In September 2007, the Human Resources Committee replaced Mercer and retained the services of Semler Brossy as its outside executive compensation advisor.'
   , {'entities': [(81,87, 'CC'), (263,269,"CC"),(299,312, 'CC')]})
, ('The Nominating Committee, working with management and third party compensation consultants and reviewing benchmarked data from a comparator group of companies, determines director compensation that it believes is competitive with these companies. The Nominating Committee periodically reviews and revises, when necessary, the Director Compensation Policy, generally with the aid of a compensation consultant. The Nominating Committee most recently revised this policy in December 2006 to formally establish compensation for the Chairman of the Board and to provide for directors’ use of motorcycles where doing so may further a company business objective.'
   , {'entities': []})
, ('In 2007, there were five regularly scheduled meetings of the Board, one of which was a telephonic meeting. With the exception of Messrs. Beattie and Zeitz, all current directors attended at least 75% of the meetings of the Board and the committees on which they served during 2007. Mr. Zeitz was only elected to the Board in August 2007. The Board met in executive sessions during all regularly scheduled meetings (except the telephonic meetings), without management present, and plans to continue that practice going forward. On April 28, 2007, non-management members of the Board re-appointed Mr. Allen as presiding director for these executive sessions.'
   , {'entities': []})
, ('Also, with the assistance of its outside advisor, the Human Resources Committee looks to a group of comparator companies that it believes to be similar to Harley-Davidson in business characteristics and economics. These companies generally focus their operations on engineering, manufacturing and the management of a strong product brand. We list below the comparator group we used in 2007. Annually, the Human Resources Committee reviews compensation levels and reward practices of these comparator companies’ based upon proxy disclosures.'
   , {'entities': []})
, ("a Participant who ceases to be employed by the Company or an Affiliate of the Company and immediately thereafter becomes a Non-Employee Director, a non-employee director of any of its Affiliates, or a consultant to the Company or any of its Affiliates shall not be considered to have terminated employment until such Participant’s service as a director of, or consultant to, the Company and its Affiliates has ceased; and"
   , {'entities': []})
, ('In general, we grant equity-based long-term incentives annually in February. In the case of the CEO, the Human Resources Committee recommends a long-term incentive for the CEO to the Nominating Committee for review and approval. The Human Resources Committee has authorized the CEO to make equity grants to employees in certain instances, including to help recruit a new employee or retain a current employee or to reward an employee for exceptional service or such other instance that the CEO believes is in our best interest. The CEO may grant awards of not more than 50,000 shares of our common stock in the aggregate annually and not more than 20,000 shares of common stock to an employee and/or a person engaged to become an employee, but may not grant equity awards to members of the Leadership and Strategy Council. The Human Resources Committee has adopted a number of policies and agreements to further the goals of the executive compensation program and to strengthen the alignment of interests of executives with the long-term interests of shareholders. These include Stock Ownership Guidelines for executives that we describe beginning on page 57. We also provide benefits to our executives that are the same benefits received by salaried employees in general. They include medical and dental benefits, retirement plans, employee savings plans, death benefits and deferred compensation plans for eligible employees. Management reviews these programs periodically, generally with the aid of an outside consultant, and revises them when necessary. In addition, the Human Resources Committee periodically reviews aspects of these programs.'
   , {'entities': []})
, ('The Nominating Committee is responsible for establishing, reviewing and revising compensation we pay to our directors. The Nominating Committee, working with management and third party compensation consultants and reviewing benchmarked data from a comparator group of companies, determines director compensation that it believes is competitive with these companies. The Nominating Committee periodically reviews and revises, when necessary, the Director Compensation Policy, generally with the aid of a compensation consultant. The Nominating Committee most recently revised this policy in December 2006 to formally establish compensation for the Chairman of the Board and to provide for directors’ use of motorcycles where doing so may further a company business objective.'
   , {'entities': []})
, ('For 2009 and into 2010, the Human Resources Committee retained the services of Semler Brossy as its outside executive compensation advisor. After a thorough review process, the Human Resources Committee hired Meridian Compensation Partners, LLC as its new outside executive compensation advisor in August 2010. We describe the independent advisor’s primary responsibilities and reporting obligations more fully in the “Corporate Governance Principles and Board Matters—Human Resources Committee” section beginning on page 41. During 2010, neither advisor performed services for the company beyond its engagement with the Human Resources Committee.'
   , {'entities': [(79,92, 'CC'), (209,244,"CC")]})
, ('In addition to the compensation data for these comparator companies, the outside executive compensation advisor provided the Human Resources Committee and management with its analysis of a broader set of data from leading compensation surveys as additional market reference points for various components of compensation for the NEOs. The additional compensation survey sources that we used for benchmarking purposes included Towers Perrin’s Executive Compensation Database and Hewitt’s Total Compensation Management Executive Compensation Survey.'
   , {'entities': []})
, ('At the 2010 annual meeting, shareholders approved the Harley-Davidson, Inc. Employee Incentive Plan, which gave us the flexibility to grant long-term cash incentive awards. In June 2010, the Human Resources Committee and, in the case of the CEO, the Nominating Committee approved long-term cash incentive awards for certain Senior Leaders including all NEOs other than Mr. Jones, who was not yet an employee. Each executive received a long-term cash incentive award with a target value equal to one-third of the total value of long-term incentives that they were eligible to receive in 2010 so that, when combined with the equity awards the executive received in February 2010, the executive received 100% of the value of long-term incentives that the executive was eligible to receive.'
   , {'entities': []})
, ('In certain special circumstances, such as for newly-hired executives or for special retention or recognition, we also provide compensation outside of these regular executive compensation programs (special equity awards for newly hired executives). For example, upon his hiring, Mr. Jones received an equity award consisting of 50,000 stock options and 15,000 restricted shares. These awards vest ratably over three years. We provided these awards to Mr. Jones to compensate him for amounts that he forfeited by leaving his prior employer.'
   , {'entities': []})
, ('For 2011, the Human Resources Committee retained the services of Meridian Compensation Partners LLC as its outside executive compensation advisor. We describe the independent advisor’s primary responsibilities and reporting obligations more fully in the “Corporate Governance Principles and Board Matters—Human Resources Committee” section beginning on page 26. During 2011, the independent outside executive compensation advisor performed no services for the company beyond its engagement with the Human Resources Committee.'
   , {'entities': [(65,99,'CC')]})
, ('he Human Resources Committee also reviewed and approved the target STIP opportunities for all NEOs for 2015. Target STIP opportunity is the amount of STIP compensation that we would pay to an NEO, expressed as a percentage of his or her annual base salary, assuming that the actual performance resulted in a payout at target. Based upon a review of competitive market data and our compensation philosophy of targeting compensation at the 50th percentile plus or minus 20% based on individual performance and experience, Mr. Wandell recommended the target STIP opportunities for each NEO other than himself. The Human Resources Committee determined the target STIP opportunities for the CEO based upon a review of external market compensation data with input from the outside executive compensation advisor. On this basis, the Committee increased Mr. Levatich’s target STIP opportunity to 115% from 110% in conjunction with his impending promotion to President and CEO. There was no change to Mr. Wandell’s STIP target for the four months of his employment in 2015 preceding his retirement. For each of the remaining NEOs, the Committee approved 2015 STIP targets that were the same as in 2014.'
   , {'entities': []})
, ('John S. Chen, Lloyd H. Dean, Susan E. Engel, Donald M. James, and Stephen W. Sanger served as members of the HRC in 2012. Mackey J. McDonald also served on the HRC prior to his retirement as a director in April 2012. During 2012, no member of the HRC was an employee, officer, or former officer of the Company. None of our executive officers served in 2012 on the board of directors or compensation committee (or other committee serving an equivalent function) of any entity that had an executive officer serving as a member of our Board or the HRC. As described under “Related Person Transactions,” all HRC members had banking or financial services transactions in the ordinary course of business with our banking and other subsidiaries.'
   , {'entities': []})
, ('Susan E. Engel, one of our directors, served as chairwoman and chief executive officer of Lenox Group Inc., a tabletop, giftware and collectibles company, from November 1996 until she retired in January 2007. In November 2008 Lenox Group filed a voluntary petition for relief under Chapter 11 in the U.S. Bankruptcy Court for the Southern District of New York. Susan G. Swenson, one of our directors, served as a director and as president and chief operating officer of Leap Wireless International, Inc., a wireless communications provider, from July 1999 to January 2004. In April 2003 Leap Wireless filed a voluntary petition for relief under Chapter 11 in the U.S. Bankruptcy Court for the Southern District of California, and in August 2004 Leap Wireless completed its financial restructuring and emerged from Chapter 11. She also served as chief operating officer of Amp’d Mobile, Inc., a mobile technology provider, from October 2006 until July 2007. In June 2007 Amp’d Mobile filed a voluntary petition for relief under Chapter 11 in the U.S. Bankruptcy Court for the District of Delaware, and in July 2007 Amp’d Mobile ceased operations and thereafter sold its assets.'
   , {'entities': []})
, ('The HRC and GNC retained Cook & Co., a nationally recognized executive compensation consulting firm, to provide independent advice on executive and non-employee director compensation matters for 2012.'
   , {'entities': [(25,35,'CC')]})
, ('Cook & Co.’s business is limited to providing independent executive compensation consulting services to its clients.'
   , {'entities': [(0,10,'CC')]})
, ('Cook & Co. does not provide any other management or human resources-related services to our Company.'
   , {'entities': [(0,10,'CC')]})
, ('To establish a framework for evaluation of the competitiveness of 2012 compensation for our named executives, the HRC reviewed data compiled by Cook & Co., the HRC’s independent compensation consultant'
   , {'entities': [(144,154,'CC')]})
, ('Cook & Co. compiles compensation data for the financial services companies the HRC considers our Labor Market Peer Group from time to time, and reviews with the HRC the Company’s executive compensation programs generally and in comparison to those of our Labor Market Peer Group.'
   , {'entities': [(0,10,'CC')]})
, ('Cook & Co. also advises the HRC on the reasonableness of our compensation levels compared to our Labor Market Peer Group, and the appropriateness of our compensation program structure in supporting the Company’s business objectives. Cook & Co.'
   , {'entities': [(0,10,'CC')]})
, ('The total amount of fees the Company paid Cook & Co. in 2013 was $157,514, which included the fees paid for services provided as the independent compensation consultant to the HRC and GNC, reimbursement of Cook & Co.’s reasonable travel and business expenses, and a fee of less than $4,000 for a survey of long-term incentives which is used for evaluating the competitiveness of long-term incentive opportunities for other positions throughout the Company.'
   , {'entities': [(42,52, 'CC'), (206,216,"CC")]})
, ('The HRC and GNC, similar to other Board committees, are authorized to retain and obtain advice of legal, accounting, or other advisors at our expense without prior permission of management or the Board. The HRC and GNC use a consultant to assist in the evaluation of executive compensation and non-employee director compensation, respectively. Under its charter, the HRC has sole authority to retain or obtain the advice of and terminate any compensation consultant, independent legal counsel or other adviser to the HRC, and approve their fees and other retention terms. The HRC and GNC charters are available on our website at: https://www.wellsfargo.com/about/corporate/corporate_governance.'
   , {'entities': []})
, ('Compensation for the Chief Executive Officer and the other executive officers named in the Summary Compensation Table consists of annual compensation (base salary and an incentive compensation award) and long-term compensation. The Committee sets base salary ranges for executive officers using available compensation data for the prior year from a comparison group of financial services organizations. It also awards annual incentive compensation, usually in cash, and long-term compensation in the form of stock options or other stock-based awards under the Company’s LTICP to the Company’s Chief Executive Officer and other executive officers. Under the Company’s pay-for-performance philosophy, the Committee believes the incentive compensation award should be at risk annually to provide strong motivation to each executive officer to achieve his or her performance goals and to contribute to the Company’s overall performance each year. Similarly, the Committee awards stock options to align the executive officer’s interest with that of stockholders in the future performance of the Company. In connection with its compensation decisions, the Committee has also retained the services, and seeks the advice and opinion of an independent consultant with respect to the Company’s executive compensation programs and pay practices. The discussion below applies generally to the 2005 annual salary, incentive compensation, and long-term compensation approved by the Committee for the executive officers named in the Summary Compensation Table. In the case of Mr. Kovacevich, as Chief Executive Officer of the Company, the Board of Directors ratifies the compensation approved by the Committee (without the Chief Executive Officer being present). A more complete description of Mr. Kovacevich’s 2005 compensation can be found below under the heading “How is the Chief Executive Officer’s compensation determined?”'
   , {'entities': []})
, ("For purposes of compiling Peer Group non-employee director compensation data and otherwise advising the GNC on compensation matters, the GNC has retained the services of George B. Paulin, Chairman and Chief Executive Officer of Frederic W. Cook & Co., Inc. (F.W. Cook), a compensation consulting firm, to act as the GNC’s independent compensation consultant."
   , {'entities': [(228,256, 'CC'), (258,267,"CC")]})
, ("For purposes of establishing director compensation for 2007, the GNC asked Mr. Paulin at its September 2006 meeting to review the Company’s director compensation program in light of Peer Group companies’ compensation data and compensation practices for their non-employee directors."
   , {'entities': [(75,85,'CC')]})
, ("Beginning in 2007, the HRC also reviewed an analysis of Peer Group compensation data prepared by its compensation consultant, F.W. Cook, using a standardized methodology for valuing equity grants."
   , {'entities': [(126,135,'CC')]})
, ("Prior to joining Coors, from April 2004 until March 2005, Mr. van Paasschen worked independently through FPaasschen Consulting, a consulting company, and Mercator Investments, a private equity firm, evaluating, proposing, and negotiating private equity transactions. Prior thereto, Mr. van Paasschen spent seven years at Nike, Inc., a designer, developer and marketer of footwear, apparel and accessory products, most recently as Corporate Vice President/General Manager, Europe, Middle East and Africa from 2000 to 2004. From 1995 to 1997, Mr. van Paasschen served as Vice President, Finance and Planning at Disney Consumer Products, a business segment of The Walt Disney Company that extends the Disney brand to a range of merchandise, and earlier in his career was a management consultant for eight years at the global management consulting firm of McKinsey & Company and the Boston Consulting Group. Mr. van Paasschen has been a director of the Company since September 2007."
   , {'entities': []})
, ("Compensation Consultants Retained — the Compensation Committee retained Meridian Compensation Partners, LLC to assist it in the review and determination of compensation awards for the Named Executive Officers."
   , {'entities': [(72,107,'CC')]})
, ("Separation Agreement with Mr. van Paasschen. On February 17, 2015, we announced that Mr. van Paasschen had resigned his positions as the President and Chief Executive Officer and as a member of the Board effective February 13, 2015. On February 16, 2015, Mr. van Paasschen entered into a Separation Agreement and General Release with us pursuant to which his employment continued until February 28, 2015 and he agreed to serve as a consultant to us from then through May 31, 2015, and under which he is entitled to receive certain payments and benefits. Our separation and consulting arrangements with Mr. van Paasschen are described in more detail below in the section entitled Potential Payments Upon Termination or Change in Control beginning on page 61 of this proxy statement."
   , {'entities': []})
, ("In the case of Mr. Mangas and Ms. Poulter, these base salary evaluations were conducted at the time those officers joined the company. Mr. Schnaid’s base salary was benchmarked in a manner substantially as described above, but because we did not expect that he would serve as our Interim Chief Financial Officer, Mr. Schnaid’s base salary was determined based on the 50th percentile for similar corporate controller and principal accounting officer positions as well as a review of the range of values around the median, including out to the 25th and 75th percentile, for reference purposes, among companies with revenue in excess of $5 billion included in a general industry survey provided by Towers Watson, the Company’s external compensation consultant."
   ,{'entities': [(695,708,'CC')]})
, ("Mr. van Paasschen has been Chief Executive Officer and President of the Company since September 2007. From March 2005 until September 2007, he served as President and Chief Executive Officer of Molson Coors Brewing Company’s largest division, Coors Brewing Company, a brewing company, prior to its merger with Miller Brewing Company and the formation of MillerCoors LLC. Prior to joining Coors, from April 2004 until March 2005, Mr. van Paasschen worked independently through FPaasschen Consulting, a consulting company, and Mercator Investments, a private equity firm, evaluating, proposing, and negotiating private equity transactions. Prior thereto, Mr. van Paasschen spent seven years at Nike, Inc., a designer, developer and marketer of footwear, apparel and accessory products, most recently as Corporate Vice President/General Manager, Europe, Middle East and Africa from 2000 to 2004. From 1995 to 1997, Mr. van Paasschen served as Vice President, Finance and Planning at Disney Consumer Products, a business segment of The Walt Disney Company that extends the Disney brand to a range of merchandise, and earlier in his career was a management consultant for eight years at the global management consulting firm of McKinsey & Company and the Boston Consulting Group. As the Company’s Chief Executive Officer and President for the past five years, Mr. van Paasschen has valuable insight into, and a unique understanding of, the Company’s operations, management and culture and provides an essential link between management and the Board on management’s business perspectives. His specific experience with the Company, combined with his extensive managerial experience and knowledge of the hotel and leisure industry generally, make him essential to developing the strategic plan for the Company."
   , {'entities': []})
, ("In determining the number of shares to request for the 2013 Plan’s share authorization, we, at the direction of the Compensation Committee, worked with Meridian Compensation Partners, LLC (“Meridian”), the Compensation Committee’s independent compensation consultant, to evaluate our recent share usage, our share availability under the 2004 Plan, our historical burn rate under the 2004 Plan, our projected burn rate under the 2013 Plan, the potential cost to stockholders of the new share request under the 2013 Plan, and the overhang cost associated with outstanding equity-based awards that we granted under the 2004 Plan."
   , {'entities': [(152,187, 'CC'), (190,198,"CC")]})
, ("The Compensation Committee has retained Mercer Human Resource Consulting as its compensation consultant to assist in the development and evaluation of compensation policies and the Compensation Committee’s determination of compensation awards."
   , {'entities': [(40,72,'CC')]})
, ("The Compensation Committee retained Pearl Meyer & Partners to assist in the review and determination of compensation awards to the Named Executive Officers (including the Chief Executive Officer) for the 2010 performance period, as well as the annual fees or other compensation paid to our Board."
   , {'entities': [(36,58,'CC')]})
, ("Pearl Meyer & Partners worked with management and the Compensation Committee in reviewing the compensation structure of the Company and of the companies in the peer group. The fees paid to Pearl Meyer & Partners for services performed for the Compensation Committee during 2010 were $136,000." 
   , {'entities': [(0,22, 'CC'), (189,211,"CC")]})
, ("Pearl Meyer & Partners does not provide any other services to the Company and no other fees were paid to Pearl Meyer & Partners by the Company during 2010."
   ,{'entities': [(0,22, 'CC'), (105,127,"CC")]})
, ("Adam M. Aron, 54, has been Chairman and Chief Executive Officer of World Leisure Partners, Inc., a leisure-related consultancy, since 2006. From 1996 through 2006, Mr. Aron served as Chairman and Chief Executive Officer of Vail Resorts, Inc., an owner and operator of ski resorts and hotels. Mr. Aron is a director of Norwegian Cruise Line Limited and Prestige Cruise Holdings, Inc. Mr. Aron has been a Director of the Company since August 2006."
   , {'entities': []})
, ("The Human Resources and Compensation Committee of the Board of Directors, all of the members of which are independent under the listing standards of the New York Stock Exchange, is responsible for establishing and implementing our executive compensation program. Management, consistent with our compensation philosophy and objectives, and working with its outside compensation consultant (Towers, Perrin, Forster & Crosby, Inc.), makes recommendations to the Committee regarding the design and implementation of our executive compensation program."
   , {'entities': [(389,427,'CC')]})
, ("In evaluating management’s recommendations, the Committee engages an independent consultant (James F. Reda and Associates, LLC) to assist in its deliberations and decision-making."
   , {'entities': [(93,126,'CC')]})
, ("Management works with its outside executive compensation consultant (Mercer LLC) in making recommendations that are consistent with the Company’s philosophy and objectives. Mercer does not work for the Committee or the Board of Directors in any capacity."
   , {'entities': [(69,79,'CC')]}) 
, ("The Committee engages an independent consultant (James F. Reda & Associates, LLC, a division of Gallagher Benefit Services) to assist in its deliberations and decision-making."
   , {'entities': [(49,80,'CC')]})
, ("Management’s current compensation consultant is Frederic W. Cook & Co., Inc. and management also consulted with Mercer LLC during fiscal 2012."
   , {'entities': [(48,76, 'CC'), (112,122,"CC")]})
, ("the Committee retained Meridian Compensation Partners LLC (Meridian) as its independent consultant."
   ,{'entities': [(23,57, 'CC'), (59,67,"CC")]})
, ("Prior to September 2013, the Committee’s independent consultant was James F. Reda & Associates, LLC, a division of Gallagher Benefit Services"
   , {'entities': [(68,99,'CC')]})
, ("The Committee uses an independent consultant, Pearl Meyer & Partners, to provide information on current developments and practices in director compensation."
   , {'entities': [(46,68, 'CC')]})
, ("Pearl Meyer & Partners is the same consultant retained by the Compensation Committee to advise on executive compensation, but performs no other work for ExxonMobil."
   , {'entities': [(0,22, 'CC')]})
, ("in 2006 the committee retained Mercer Human Resources Consulting and Towers Perrin to provide advice, their opinions, and resources to help develop and execute our overall compensation strategy."
   , {'entities': [(31,64, 'CC'), (69,82,"CC")]})
, ("From June 1992 to August 1992, Mr. Bannick served as a consultant for McKinsey & Company, a consulting firm, in Europe and from June 1993 to April 1995 in the U.S. Mr. Bannick also served as a U.S. diplomat in Germany during the period of German unification. Mr. Bannick holds a B.A. in Economics and International Studies from University of Washington and an M.B.A degree from the Harvard Business School."
   , {'entities': []})
, ("As discussed above, in 2007 the committee retained Towers Perrin to provide advice, its opinion, and resources to help develop and execute our overall compensation strategy."
   , {'entities': [(51,64, 'CC')]})
, ("Pay Governance serves as the Compensation Committee’s independent compensation consultant"
   , {'entities': [(0,14, 'CC')]})
, ("Mr. Moffett currently serves on the Board of Directors of CIT Group Inc. (where he currently serves as a member of the Compensation Committee) and of Genworth Financial, Inc. (where he currently serves as a member of the Nominating and Corporate Governance Committee and as a member of the Legal and Public Affairs Committee). He also currently serves as a Trustee for Columbia Atlantic Mutual Funds and University of Oklahoma Foundation and as a consultant to various financial services companies."
   , {'entities': []})
, ("In 2010, the committee selected Pay Governance LLC as its independent compensation consultant."
   , {'entities': [(32,50, 'CC')]})
, ("In February 2010, the committee decided to replace Towers Watson & Co. with Pay Governance LLC as its independent compensation consultant."
   , {'entities': [(51,70, 'CC'), (76,94,"CC")]})
, ("The Company does not currently retain executive compensation consultants."
   , {'entities': []})
, ("We and Mr. Hull are parties to a consulting agreement pursuant to which, upon his retirement, he will become a consultant to the Company for a period of four years at a fixed consulting fee that will decline from $275,000 in the first year to $100,000 in the fourth year, and he will remain entitled to certain customary benefits that we provide to employees during the term of that agreement."
   , {'entities': []})
, ("Myrtle S. Potter, age 48, has been a director of the Company since April 2004. Ms. Potter has been Chief Executive Officer of Chapman Properties, Inc., a group of real estate sales, financing and development companies, since September 2006, and a consultant with Myrtle Potter Consulting, LLC, a healthcare consulting company, since August 2005."
   , {'entities': []})
, ("The Board adopted the 1999 Nonofficer Employee Stock Option Plan (the “1999 Plan”) to enable the grant of nonqualified stock options to employees, consultants, agents, advisors and independent contractors of the Company and its subsidiaries who are not officers or Directors of the Company."
   , {'entities': []})
, ("The Leadership Development and Compensation Committee has delegated authority to make grants under the 1999 Plan to another committee of the Board and to certain officers of the Company, subject to specified limitations on the size and terms of such grants."
   , {'entities': []})
, ("At Genentech, Inc. Ms. Potter was President, Commercial Operations, from March 2004 to August 2005 and Executive Vice President, Commercial Operations and Chief Operating Officer from May 2000 to March 2004. Ms. Potter is also a director of FoxHollow Technologies, Inc."
   , {'entities': []})
,("Arthur D. Levinson, Ph.D. has been the Chief Executive Officer and a Director of Genentech Inc. (“Genentech”) since July 1995. Dr. Levinson has been the Chairman of the Board of Directors of Genentech since September 1999. He joined Genentech in 1980 and served in a number of executive positions, including the Senior Vice President of Research and Development from 1993 to 1995. Dr. Levinson is also a member of the Board of Directors of Google."
  , {'entities': []})
,("In April 2010, Messrs. Szkutak, Jassy, Piacentini and Wilke received restricted stock unit awards with vesting beginning in May 2014, assuming continued employment. Mr. Szkutak received a restricted stock unit award for 46,000 shares. In making this grant, the Leadership Development and Compensation Committee considered the factors discussed above with respect to periodic grants, including Mr. Szkutak’s experience and skill as Chief Financial Officer, his sustained performance over time in years preceding the grant, and his expected future contributions. Mr. Jassy received a restricted stock unit award for 46,000 shares. In making this grant, the Leadership Development and Compensation Committee considered the factors discussed above with respect to periodic grants, including Mr. Jassy’s experience and skill in managing web services and cloud computing operations, his sustained performance over time in years preceding the grant, and his expected future contributions. Mr. Piacentini received a restricted stock unit award for 46,000 shares. In making this grant, the Leadership Development and Compensation Committee considered the factors discussed above with respect to periodic grants, including Mr. Piacentini’s experience and skill in managing international retail operations, his sustained performance over time in years preceding the grant, and his expected future contributions. Mr. Wilke received a restricted stock unit award for 50,000 shares. In making this grant, the Leadership Development and Compensation Committee considered the factors discussed above with respect to periodic grants, including Mr. Wilke’s experience and skill in managing North American retail operations, his sustained performance over time in years preceding the grant, and his expected future contributions."
  , {'entities': []})
,("Millard Drexler has been Chairman and Chief Executive Officer of J.Crew Group, Inc. (“J.Crew”) since January 2003. Previously, Mr. Drexler was Chief Executive Officer of The Gap, Inc. (“Gap”) from 1995 and President from 1987 to September 2002. Mr. Drexler also was a director of Gap from November 1983 to October 2002. Among other qualifications, Mr. Drexler brings to the Board executive leadership experience, including his service as a chief executive officer of a public company, along with extensive brand marketing experience."
  , {'entities': []})
, ("Al Gore has served as Executive Chairman of Current TV since 2002, Chairman of Generation Investment Management since 2004, and a partner of Kleiner Perkins Caufield & Byers since 2007. Mr. Gore also is Chairman of the Climate Reality Project. Among other qualifications, Mr. Gore brings to the Board executive leadership experience, a valuable and different perspective due to his extensive background in politics, government and environmental rights, along with experience in asset management and venture capital."
   , {'entities': []})   
, ("Robert Iger has served as President and Chief Executive Officer of The Walt Disney Company (“Disney”) since October 2005, having previously served as President and Chief Operating Officer since January 2000 and as President of Walt Disney International and Chairman of the ABC Group from 1999 to January 2000. Prior to that, from 1974 to 1998, Mr. Iger held a series of positions with increasing responsibility at ABC, Inc. and its predecessor Capital Cities/ABC, Inc. Mr. Iger is a member of the board of directors of the National September 11 Memorial & Museum, the Lincoln Center for the Performing Arts, and the U.S.-China Business Council. Since June 2010, Mr. Iger has also served on the President’s Export Council. Among other qualifications, Mr. Iger brings to the Board executive leadership experience, including his service as a chief executive officer of a large public company, along with extensive financial expertise and experience in international exports and brand marketing."
   , {'entities': []}) 
, ("Andrea Jung joined Avon Products, Inc. (“Avon”) in January 1994. Ms. Jung was Chairman of the Board of Directors and Chief Executive Officer of Avon from September 2001 until April 2012 when she assumed the role of Executive Chairman. In October 2012, Ms. Jung announced that, effective as of December 31, 2012, she would step down as Executive Chairman and as a board member of Avon and thereafter assume a position as a senior advisor to the board of directors of Avon. She had previously served as Chief Executive Officer since November 1999 and was a member of the board of directors of Avon since January 1998. Ms. Jung has also been a director of General Electric Company since 1998, where she serves on the Management Development and Compensation Committee and the Nominating and Corporate Governance Committee. She also is a member of the New York Presbyterian Hospital Board of Trustees, a director of Catalyst, a nonprofit corporate membership research and advisory organization, and Vice Chairman of the World Federation of Direct Selling Associations. Among other qualifications, Ms. Jung brings to the Board executive leadership experience, including her service as a chief executive officer of a large public multinational company, along with extensive brand marketing and consumer products experience."
   , {'entities': []}) 
, ("Arthur Levinson has been Chairman of Genentech, Inc. (“Genentech”) since September 1999. Previously, Dr. Levinson also served as Chief Executive Officer of Genentech from July 1995 to April 2009. Since May 2009, Dr. Levinson has served as an advisor to Genentech’s Research and Early Development center and as a member of the Scientific Resource Board, Genentech’s external advisory group. Dr. Levinson is a director of NGM Biopharmaceuticals, Inc. He also serves as a director of Amyris, Inc., on the Board of Scientific Consultants of the Memorial Sloan-Kettering Cancer Center, on the Industrial Advisory Board of the California Institute for Quantitative Biomedical Research, on the Advisory Council for the Princeton University Department of Molecular Biology, on the Advisory Council for the Lewis-Sigler Institute for Integrative Genomics, and on the Executive Council of TechNet. Dr. Levinson previously served as a director of Google Inc. from April 2004 until October 2009. Among other qualifications, Dr. Levinson brings to the Board executive leadership experience, including his service as a chairman of a public company, along with extensive financial expertise and brand marketing experience."
   , {'entities': []}) 
, ("Ronald Sugar is the retired Chairman of the Board and Chief Executive Officer of Northrop Grumman Corporation (“Northrop Grumman”). Dr. Sugar was Chairman of the Board and Chief Executive Officer of Northrop Grumman Corporation from 2003 until 2010 and President and Chief Operating Officer from 2001 until 2003. He was President and Chief Operating Officer of Litton Industries, Inc. from 2000 until the company was acquired by Northrop Grumman in 2001. He was earlier Chief Financial Officer of TRW Inc. Dr. Sugar has also been a director of Air Lease Corporation since 2010, of Amgen Inc. since July 2010, and of Chevron Corporation since April 2005. Dr. Sugar is a member of the National Academy of Engineering, trustee of the University of Southern California, director of the Los Angeles Philharmonic Association and national trustee of the Boys and Girls Clubs of America. Among other qualifications, Dr. Sugar brings to the Board executive leadership experience as a chairman and chief executive officer of a major public company, financial expertise as a former chief financial officer, understanding of advanced technology, and a global business perspective from his service on other boards."
   , {'entities': []})
, ("Waleed Muhairi—Mr. Muhairi, 37, has been a director since March 2009. Mr. Muhairi brings to our Board his experience in international markets and channels relevant to our business as well as his expertise in operations, finance and strategic consulting. Since 2006, Mr. Muhairi has been the Chief Operating Officer of Mubadala Development Company PJSC (“Mubadala”), a strategic investment and development company owned by the Government of Abu Dhabi, United Arab Emirates, where he oversees Mubadala’s broad investment portfolio and is responsible for its strategic, operational and business development activities. Mr. Muhairi is also a member of Mubadala’s Investment Committee, whose mandate is to develop Mubadala’s investment policies, establish investment guidelines and review all proposed projects and investments to ensure they are in line with Mubadala’s business objectives. Since September 2008, Mr. Muhairi has been the Chairman of Advanced Technology Investment Company LLC, a company wholly owned by Mubadala, mandated to make significant investments in the advanced technology sector, locally and internationally, with a view of delivering long-term economic and social benefits to the Emirate of Abu Dhabi, the Middle East and beyond. Prior to his roles with Mubadala and ATIC, Mr. Muhairi worked with the UAE Offsets Program Bureau as a Senior Projects Manager and with McKinsey & Company as a commercial and governmental consultant."
   , {'entities': []})
, ("The Compensation Committee, with assistance from its independent executive compensation consultant and counsel, has structured our executive compensation program to reflect our “pay-for-performance” philosophy. A significant portion of the compensation opportunities provided to the Named Executive Officers are dependent on our financial performance, which are intended to drive the creation of stockholder value. The Compensation Committee intends to continue to emphasize responsible compensation arrangements that attract, retain and motivate high caliber executive officers, motivate these executive officers to achieve our short-term and long-term business strategies and objectives and support career development and succession goals."
   , {'entities': []})
, ("The Compensation Committee reviews and certifies our level of achievement for each performance measure before any payments are made. This review and certification is generally performed at the first regularly scheduled Compensation Committee meeting following the end of the year with any payout of the annual cash performance bonus occurring in March 2015. Under the terms of the EIP, the Compensation Committee has the authority to reduce any Named Executive Officer’s annual cash performance bonus prior to payment. For 2014, the Compensation Committee did not exercise this authority in connection with any of our Named Executive Officers."
   , {'entities': []})
, ("The Compensation Committee reduced the target annual cash performance bonus opportunity of Mr. Seifert under the EIP from 150% to 100%, to more closely align his target annual cash bonus opportunity with the target annual cash bonus opportunities of other chief financial officers whose total direct compensation opportunity (i.e., base salary, target cash performance bonus opportunity, and target value of long-term equity awards) fell between the 50th and 75th percentile of the competitive market data compiled by Compensia."
   , {'entities': [(518,527, 'CC')]})
, ("The Compensation Committee made the following design changes to the annual cash performance bonus opportunities under the EIP"
   , {'entities': []})
, ("For 2012, with the exception of Mr. Byrne, each Named Executive Officer’s annual cash performance bonus under the EIP was determined based on our performance during two semi-annual performance periods (i.e., January 1, 2012 to June 30, 2012 and July 1, 2012 to December 29, 2012). Mr. Byrne’s annual cash performance bonus under the EIP was determined based on our performance during the second semi-annual performance period as he was not eligible to participate in the EIP for the first semi-annual performance period. These performance bonuses, if earned, are paid in a single lump-sum payment after the end of the year."
   , {'entities': []})
, ("Generally, short-term incentives, in the form of an annual cash performance bonus, are provided to the Named Executive Officers under the EIP, and are intended to focus the Named Executive Officers on our short-term business objectives and strategies."
   , {'entities': []})
, ("Under the EIP, the amount of the Named Executive Officers’ annual cash performance bonus, if any, depends on our performance during the respective performance period, as evaluated against pre-established target levels under one or more financial measures. The financial measures and related target levels for a given performance period are approved by the Compensation Committee shortly after the commencement of the performance period."
   ,  {'entities': []})
, ("The Compensation Committee, with assistance from its independent executive compensation consultant and counsel, has structured our executive compensation program to reflect our “pay-for-performance” philosophy."
   , {'entities': []})
, ("We believe that the quality, skills, engagement and dedication of our senior leadership team, including our Named Executive Officers, are vital to the successful execution of each phase and milestone of our transformation plan and other key objectives that are designed to continue to drive stockholder value. As we explain in detail below, we believe that our 2013 executive compensation program successfully supported the execution of our turnaround plan and other business objectives, demonstrated our strong pay-for-performance philosophy and further aligned the interests of our Named Executive Officers with those of our stockholders."
   , {'entities': []})
, ("Annual cash performance bonuses for the Named Executive Officers are provided under our Executive Incentive Plan (the “EIP”). For the fiscal 2013 EIP, the Compensation Committee replaced non-GAAP gross margin with adjusted non-GAAP free cash flow and replaced non-GAAP net income with adjusted non-GAAP net income, as financial measures upon which the annual cash performance bonuses would be determined. The Compensation Committee also changed the performance period under the EIP from two semiannual performance periods to a single annual performance period and made the payment of any annual cash performance bonus under the EIP contingent on our maintaining a cash balance (i.e., cash, cash equivalents and marketable securities, including long-term marketable securities) of at least $700 million on the last day of each quarter of fiscal 2013. These changes were intended to more closely align the bonus opportunities under the EIP with the objectives and timeline of our transformation plan."
   , {'entities': []})
, ("Currently, U.S. stock exchange listing standards require shareholder approval of equity-based compensation plans; those plans, however, set general parameters and accord the compensation committee substantial discretion in making awards and establishing performance thresholds for a particular year. Shareholders do not have any mechanism for providing ongoing feedback on the application of those general standards to individual pay packages. (See Lucian Bebchuk & Jesse Fried, Pay Without Performance, 2004.)"
   ,{'entities': []} )
, ("The Company’s executive compensation program for the named executive officers consists of long-term equity awards in the form of restricted stock units (“RSUs”) and cash compensation in the form of performance-based cash incentives and base salaries. Each year, the Compensation Committee, which is made up entirely of independent directors, determines the compensation for the named executive officers."
   , {'entities': []})
, ("The Company relies heavily on long-term equity awards to attract and retain an outstanding executive team and to ensure a strong connection between executive compensation and financial performance. An RSU award gives the named executive officer the right to receive, at no cost, a specified number of shares of the Company’s common stock when the award vests, typically at intervals of two to four years. Because the value of the RSUs depends on the Company’s future share price, the award links compensation to future financial performance. The officer is generally not eligible to receive the shares if employment is terminated before the RSUs vest. The Compensation Committee reviews annually the outstanding, unvested equity awards of each named executive officer to determine, in the Compensation Committee’s discretion, whether additional awards are warranted in light of the officer’s performance, the competitive environment and the other factors discussed in the section entitled “Executive Compensation Program Design and Implementation—3. The Crucial Role of Long-Term Equity Awards” below."
   , {'entities': []})
, ("An RSU award generally vests only if the named executive officer continues employment until the specified vesting date, typically two to four years after the date of grant. Equity awards also help to ensure a strong connection between executive compensation and the Company’s financial performance because the value of RSUs depends on the Company’s future share price."
   , {'entities': []})
, ("From time to time, the Compensation Committee has considered various forms of performance-based vesting. After careful evaluation, the Compensation Committee has concluded that performance-based vesting would not serve the Company’s current objectives as effectively as the program described above. The Compensation Committee generally grants RSUs with two to four year vesting periods to maximize the award’s retention value. This retention value would be undermined if a named executive officer’s equity awards (which represent approximately 85% of the officer’s compensation) were at risk based on performance measures that were determined two or even four years prior to the vesting date. Given the intensely dynamic business environment in which the Company operates, it would be extremely difficult to craft meaningful objectives with such a long horizon. The Company imposes no requirement that the named executive officers hold their common stock for any period after vesting."
   , {'entities': []})
, ("The RSUs do not qualify as performance-based compensation for purposes of Section 162(m) because vesting is based on continued employment rather than specific performance goals."
   , {'entities': []})
, ("The current members of the Committee are: Mr. Henderson (Chairman), Dr. Amelio, Mr. Blanchard, Mr. Eby, Jr., and Ms. Upton. Mr. Blanchard joined the Committee in January 2007."
   , {'entities': []})
, ('The Compensation Committee consists of Mr. Bruce L. Claflin, as Chair, Mr. Robert B. Palmer, and Dr. Leonard M. Silverman, each determined by the Board to be independent. Dr. Silverman served as Chair of the Committee until May 5, 2006, when Mr. Claflin was appointed as Chair. Mr. David J. Edmondson served as a member from April 28, 2005 until his resignation from the Board of Directors effective February 24, 2006. Upon Dr. Silverman’s retirement from the Board of Directors in May 2007 and following Mr. Topfer’s re-election to the Board, Mr. Morton L. Topfer will join the Compensation Committee. During 2006, the Compensation Committee met eight times. The Compensation Committee assists the Board in discharging its responsibilities relating to the compensation of our executives and members of the Board. In consultation with management, the Board and the Compensation Committee’s compensation consultant, the Compensation Committee designs, recommends to the Board for approval and evaluates employment, severance and change of control agreements with executive officers and our compensation plans, policies and programs. The Compensation Committee ensures that compensation programs are designed to encourage high performance, promote accountability and align employee interests with the Company’s strategic goals and with the interests of our stockholders. All members of the Compensation Committee attended at least 75 percent of the meetings of the Compensation Committee in 2005.'
   ,{'entities': []})
, ('Mr. Claflin, 56, has been a director since 2003. Mr. Claflin was President, Chief Executive Officer, and a member of the Board of Directors of 3Com Corporation (3Com), a provider of voice and data networking products and services, from January 2001 until he retired in 2006. He joined 3Com as President and Chief Operating Officer in August of 1998. Prior to 3Com, Mr. Claflin served as Senior Vice President and General Manager, sales and marketing, for Digital Equipment Corporation (Digital). Mr. Claflin also worked for 22 years at IBM, where he held various sales, marketing and management positions, including general manager of IBM PC Company’s worldwide research and development, product and brand management, as well as president of IBM PC Company Americas. Mr. Claflin is a member of the Board of Directors of Ciena Corporation.'
   , {'entities': []})
, ('In connection with the acquisition by the Company of ATI Technologies Inc. effective on October 25, 2006, the Board of Directors increased the authorized number of directors from seven to nine directors and appointed Mr. John E. Caldwell and Dr. James D. Fleck to serve as members of the Board. On February 28, 2007, the Board of Directors determined that upon the 2007 Annual Meeting of Stockholders the authorized number will be reduced to seven. Dr. Leonard M. Silverman, who served the Company as a director since 1994, and Dr. Fleck, who joined our board as a result of the ATI acquisition, will not stand for election. All directors are elected annually and serve a one-year term until the next Annual Meeting. The Nominating and Corporate Governance Committee of the Board of Directors selected, and the Board of Directors accepted, the following seven persons as nominees for election to the Board: Dr. Hector de J. Ruiz, Dr. W. Michael Barnes, Mr. John E. Caldwell, Mr. Bruce L. Claflin, Ms. H. Paulett Eberhart, Mr. Robert B. Palmer and Mr. Morton L. Topfer. All of the nominees are currently directors of AMD. Mr. Caldwell joined our board as a result of the ATI acquisition and will stand for election pursuant to the ATI acquisition agreement. The Board of Directors expects all nominees named below to be available for election. If a nominee declines or is unable to act as a director, your proxy may vote for any substitute nominee proposed by the Board. Your proxy will vote FOR the election of these nominees, unless you instruct otherwise. Directors are strongly encouraged to attend annual meetings of our stockholders and all of our current Board member nominees are expected to be present at the 2007 Annual Meeting. All of our 2006 Board member nominees were present at the 2006 Annual Meeting. The experience and background of each of the nominees follows: Dr. Hector de J. Ruiz—Dr. Ruiz, 61, has been a director since 2000. Dr. Ruiz is currently our Chairman of the Board and Chief Executive Officer. Dr. Ruiz joined AMD as President and Chief Operating Officer in January 2000 and became our Chief Executive Officer on April 25, 2002. Before joining AMD, Dr. Ruiz served as President of the Motorola, Inc. Semiconductor Products Sector since 1997. From 1991 to 1995, Dr. Ruiz was Senior Vice President and General Manager of Motorola’s paging and messaging businesses and in 1996 became Executive Vice President and General Manager of those businesses. Dr. Ruiz joined Motorola in 1977 and, from 1977 to 1991, he held various executive positions in Motorola’s Semiconductor Products Sector. Before joining Motorola, Dr. Ruiz worked at Texas Instruments, Inc. from 1972 to 1977. Dr. Ruiz is a member of the Board of Directors of Eastman Kodak Company and Spansion Inc. Dr. W. Michael Barnes—Dr. Barnes, 64, has been a director since 2003. Dr. Barnes served as Senior Vice President and Chief Financial Officer of Rockwell International Corporation (Rockwell), a diversified NYSE company, from 1991 until his retirement in 2001. Dr. Barnes joined Collins Radio Company (Collins) in 1968 as a member of the corporate operations research staff. Collins was acquired by Rockwell in 1973, and Dr. Barnes held various management positions at Rockwell until 1991. He was named a distinguished alumnus by the Texas A&M University College of Engineering in 1992, is a member of the Texas A&M University Chancellor’s Century Council and is on the university’s Engineering Advisory Board. Dr. Barnes is a member of the Board of Directors of MetroPCS, Inc. John E. Caldwell—Mr. Caldwell, 56, has been a director since October 2006. Mr. Caldwell is currently a member of the Board of Directors and Chief Executive Officer of SMTC Corporation, an electronics manufacturing services company and has held these positions since October of 2003. Before joining SMTC, Mr. Caldwell held positions in the Mosaic Group, a marketing services provider, as Chair of the Restructuring Committee of the Board from October 2002 to September 2003 and in GEAC Computer Corporation Limited, a computer software company, as President and Chief Executive Officer from October 2000 to December 2001. Mr. Caldwell was a director of ATI Technologies Inc. until October 25, 2006, when the ATI acquisition was completed. Currently he is a director of Faro Technologies, Inc., a producer of three dimensional manufacturing.'
   , {'entities': []})
, ('Bruce L. Claflin—Mr. Claflin, 55, has been a director since 2003. Mr. Claflin was President, Chief Executive Officer, and a member of the Board of Directors of 3Com Corporation (3Com), a provider of voice and data networking products and services, from January 2001 until he retired in 2006. He joined 3Com as President and Chief Operating Officer in August of 1998. Prior to 3Com, Mr. Claflin served as Senior Vice President and General Manager, sales and marketing for Digital Equipment Corporation (Digital). Mr. Claflin also worked for 22 years at IBM, where he held various sales, marketing and management positions, including general manager of IBM PC Company’s worldwide R&D, product and brand management, as well as president of IBM PC Company Americas. Mr. Claflin is a member of the Board of Directors of Ciena Corporation. H. Paulett Eberhart—Ms. Eberhart, 53, has been a director since 2004. Ms. Eberhart is President and Chief Executive Officer of Invensys Process Systems, a provider of products, service and solutions for the automation and optimization of plant operation in the process industries. Before joining Invensys Process Systems, Ms. Eberhart was the President—Americas of Electronic Data Systems Corporation (EDS), an information technology and business process outsourcing company, from 2003 until she retired from EDS in 2004. Ms. Eberhart was an employee of EDS since 1978. Prior to serving as President—Americas, Ms. Eberhart was the Senior Vice President—EDS and President—Solutions Consulting. From 2001 to 2002, Ms. Eberhart served as the Senior Vice President, Information Solutions, U.S. and from 1999 to 2001 as the Senior Vice President, Information Solutions, Southwest Region. In 1998, she was the Senior Vice President, Finance. She was a member of the Board of Directors of AT Kearney, a subsidiary of EDS. Between 1978 and 1998, Ms. Eberhart served in various management positions in the area of Finance at EDS. Ms. Eberhart served as the chair of the Political Action Committee for EDS and is a member of the Financial Executives Institute and American Institute of Certified Public Accountants. Ms. Eberhart is a member of the Board of Directors of Anadarko Petroleum Corporation and Solectron Corporation. Robert B. Palmer—Mr. Palmer, 66, has been a director since 1999. Mr. Palmer was the Chairman and Chief Executive Officer of Digital Equipment Corporation (Digital) from 1995 until his retirement in 1998. Mr. Palmer was appointed Chief Executive Officer and President of Digital in October 1992. From 1985 to 1992, Mr. Palmer served in various executive positions at Digital. Before Digital, Mr. Palmer was Executive Vice President of Semiconductor Operations at United Technologies Corporation (UTC), joining UTC in 1980 when it acquired Mostek Corporation, where he was a member of the founding team in 1969. Mr. Palmer is on the Board of Trustees of the Cooper Institute for Aerobic Research, a non-profit preventative medicine research and education organization. Morton L. Topfer—Mr. Topfer, 70, has been a director since February 2005. Mr. Topfer is the Managing Director of Castletop Capital L.P., an investment firm that focuses on private equity and real estate investments. Before forming Castletop Capital in 2002, Mr. Topfer was Vice Chairman of Dell Computer Corporation, counselor to Dell’s Chief Executive Officer and a member of Dell’s office of the Chief Executive Officer. Before joining Dell in 1994, Mr. Topfer held various positions with Motorola, Inc., last serving as Corporate Executive Vice President and President of the Land Mobile Products Sector. Before joining Motorola in 1971, Mr. Topfer spent 11 years with RCA Laboratories in various research and development and management positions. Mr. Topfer serves on the Board of Directors of Measurement Specialties, Inc.'
   , {'entities': []})
, ('Consideration of Stockholder Nominees for Director. The policy of the Nominating and Corporate Governance Committee is to consider properly submitted stockholder nominations for candidates to serve on our Board. Pursuant to our bylaws, stockholders who wish to nominate persons for election to the Board of Directors at the 2008 Annual Meeting must be a stockholder of record when they give us notice, must be entitled to vote at the meeting and must comply with the notice provisions in our bylaws. A stockholder’s notice must be delivered to our Corporate Secretary not less than '
   , {'entities': []})
, ('On February 8, 2007, the Board of Directors approved an amendment to the Company’s Bylaws to change the plurality vote standard for the election of directors to a majority vote standard with respect to uncontested elections. The new standard requires each director to receive a majority of the votes cast to be elected. A majority of the votes cast means that the number of votes cast “for” a director must exceed the number of votes cast “against” that director. Previously, in uncontested elections, directors were elected under a plurality vote standard, which meant that the candidates receiving the highest number of votes were elected whether or not they received a majority of the votes cast. In contested elections, where the number of nominees exceeds the number of directors to be elected, the vote standard will continue to be a plurality of votes cast. Incumbent directors will submit a written resignation to the Board which will be effective if he/she does not receive a majority of the votes cast and the resignation is accepted by the Board.'
   , {'entities': []})
, ('The Board of Directors has adopted Principles of Corporate Governance (Principles) to address significant corporate governance issues. The Principles provide a framework for our corporate governance matters and include topics such as Board and Board committee composition and evaluation. The Nominating and Corporate Governance Committee is responsible for reviewing the Principles and reporting and recommending any changes to the Principles to the Board of Directors.'
   , {'entities': []})
, ('The Principles provide that a majority of the members of the Board must meet the criteria for independence as required by applicable law and the NYSE listing standards. No director qualifies as independent unless the Board of Directors determines that the director has no direct or indirect material relationship with the Company. On an annual basis, each director and executive officer is obligated to complete a Director and Officer Questionnaire which requires disclosure of any transactions with the Company in which the director or executive officer, or any member of his or her immediate family, have a direct or indirect material interest. The Company also independently reviews the relationship of the Company to any entity employing a director or on which the director serves as a member of the Board of Directors. Our Board of Directors has determined that all directors who served during our 2006 fiscal year and all of our director nominees, other than Dr. Ruiz, are independent in accordance with SEC and the NYSE rules. The Board has concluded that there are no business relationships that are material or that would interfere with the exercise of independent judgment by any of the directors in his or her service on the Company’s Board of Directors or the Audit Committee.'
   , {'entities': []})
, ('Each of the Committees described below has adopted a charter, which has been approved by the Board of Directors. You can access our bylaws, the latest Committee Charters, the Principles of Corporate Governance, the Worldwide Standards of Business Conduct and the Code of Ethics at the Investor Relations Web page of our Web site at www.amd.com or by writing to us at Corporate Secretary, AMD, One AMD Place, P.O. Box 3453, M.S. 68, Sunnyvale, California 94088, or emailing us at Corporate.Secretary@amd.com. We will provide you with this information free of charge. Please note that information contained on our Web site is not incorporated by reference in, or considered to be a part of, this document.'
   , {'entities': []})
, ('t is AMD’s belief that equity compensation, combined with stock ownership guidelines, aligns the perspectives of its Officers with stockholder interests. To that end, the majority of incentive compensation and total compensation in general, is delivered in equity. Prior to 2006, AMD delivered long-term compensation to Officers primarily in the form of stock options. In 2005, after considering the accounting treatment of stock options under FAS 123(R), as well as retention, talent and competitive landscape factors, the Committee approved the regular use of restricted stock units (RSUs) and the introduction of the AMD 2005 Long-Term Incentive Plan. AMD currently uses three forms of long-term incentive compensation for its Officers: stock options (options), RSUs and performance-based RSUs (see the long-term incentive design details below for more of the specific features of each vehicle). The mix of stock options, RSUs and performance-based RSUs focuses Officers on the Company’s share price. Also, using these vehicles puts more compensation at risk for the Officers, and provides for greater rewards if superior performance is generated. The actual mix of these long-term incentives was determined using competitive long-term incentive mixes as applicable for each Officer. When determining the mix between equity and cash compensation, the Committee principally considers market competitive levels, historical AMD practices, AMD’s pay for performance philosophy, Named Executive Officer'
   , {'entities': []})
, ('As part of the overall compensation structure, each Named Executive Officer has been assigned an annual share-based guideline of stock option equivalents. Before 2005, the award was delivered solely in options. Beginning in 2005, the Committee added RSUs to the program, and each Officer’s annual equity is now awarded 50% in stock options and 50% in RSUs at a 2.5-to-1 option-to-RSU ratio. For Mr. Meyer and Mr. Richard, the equity grant is more heavily weighted toward RSUs due to Mr. Meyer’s promotion and role-specific retention issues for Mr. Richard. The stock-option equivalents are granted in four separate installments throughout the year where each installment includes a grant of options and RSUs. The four-installment grant of stock incentives allows the awards to be priced throughout the year, thereby limiting volatility in cost to the Company and in opportunity to the Officer from year to year. In 2006, each installment was granted on a pre-determined date corresponding with the dates of regularly-scheduled Compensation Committee meetings, which were established in 2005. Going forward, AMD intends to grant equity awards on the 15th of the month following pre-determined dates of Compensation Committee meetings. The 2007 meeting schedule has already been determined.'
   , {'entities': []})
, ('The Compensation Committee oversees AMD’s executive compensation program under a compensation philosophy.'
   , {'entities': []})
, ('the Committee approved the use of new pay and LTIP performance groups at the beginning of 2007.'
   , {'entities': []})
, ('the Committee approved the regular use of restricted stock units (RSUs) and the introduction of the AMD 2005 Long-Term Incentive Plan. AMD currently uses three forms of long-term incentive compensation for its Officers: stock options (options), RSUs and performance-based RSUs (see the long-term incentive design details below for more of the specific features of each vehicle). The mix of stock options, RSUs and performance-based RSUs focuses Officers on the Company’s share price. Also, using these vehicles puts more compensation at risk for the Officers, and provides for greater rewards if superior performance is generated. The actual mix of these long-term incentives was determined using competitive long-term incentive mixes as applicable for each Officer. When determining the mix between equity and cash compensation, the Committee principally considers market competitive levels, historical AMD practices, AMD’s pay for performance philosophy, Named Executive Officer.'
   , {'entities': []})
, ('The overall bonus payout for the executive officers was determined by the 2006 first and second half performance results, weighted equally. In the first half of 2006, AMD performed at 1.25x target, however the Committee used downward discretion to fund this half of the bonus at 0.90x target because the Company did not achieve specified internal targets. In the second half of 2006, AMD performed under threshold. The Committee used its discretion to fund the second half portion of the bonus at 0.25x target since the primary reason for being under threshold was the strategic defense of the Company’s market share against competitive assault. This portion of the bonus will not be deductible under 162m legislation.'
   , {'entities': []})
, ('Annually, the Committee approves a bonus of 0x-4x the target award for each Officer, based on Company and individual performance against the pre-determined goals. Under the plan, the Committee is allowed full discretion to reduce the amount of any award prior to payment as a result of the participant’s performance during the award period.'
   , {'entities': []})
, ('To fund long-term compensation programs, the Committee reviews and provides guidance around an equity pool available for awards in any given year at the median level of competitive market practices. For 2006, the Committee targeted a total annual share dilution rate of 2.5%. For 2007, the Committee has approved a total target annual share dilution rate of 3%. The Committee believes that this dilution rate is necessary to provide competitive equity grants, particularly in light of the increased employee population as a result of the acquisition of ATI Technologies Inc. This dilution rate is also within competitive norms.'
   , {'entities': []})
, ('the Committee added RSUs to the program, and each Officer’s annual equity is now awarded 50% in stock options and 50% in RSUs at a 2.5-to-1 option-to-RSU ratio.'
   , {'entities': []})
, ('The Compensation Committee of the Board of Directors has reviewed and discussed with management the Compensation Discussion and Analysis included in this proxy statement. Based on this review and discussion, the Committee recommended to the Board of Directors that the Compensation Discussion and Analysis be included in the Company’s proxy statement for the Company’s 2007 annual meeting of stockholders.'
   , {'entities': []})
, ('The Audit Committee oversees AMD’s internal audit function and independent registered public accounting firm and assists the Board in fulfilling its oversight responsibilities on matters relating to the integrity of AMD’s financial statements, AMD’s compliance with legal and regulatory requirements and the independent registered public accounting firm’s qualifications and independence by meeting regularly with the independent registered public accounting firm, internal audit, financial management and legal and other personnel. Management is responsible for the preparation, presentation and integrity of the Company’s financial statements. The independent registered public accounting firm is responsible for performing an audit of the Company’s annual financial statements and expressing an opinion as to the conformity of the Company’s audited financial statements with generally accepted accounting principles.'
   , {'entities': []})
, ('In fulfilling its oversight responsibilities, the Audit Committee reviewed and discussed the Company’s audited financial statements for the fiscal year ended December 31, 2006, with AMD management and Ernst & Young LLP, our independent registered public accounting firm. The Audit Committee also discussed with Ernst & Young LLP the matters required to be discussed by Statement on Auditing Standards No. 61 (Communications with Audit Committees, as amended by Statement on Auditing Standards No. 90 (Audit Committee Communications)). This included a discussion of the independent registered public accounting firm’s judgments as to the quality, not just the acceptability, of the Company’s accounting principles and such other matters that generally accepted auditing standards require to be discussed with the Audit Committee. The Audit Committee also received the written disclosures and the letter from Ernst & Young LLP required by Independence Standards Board Standard No. 1 (Independence Discussion with Audit Committees) and the Audit Committee discussed the independence of Ernst & Young LLP with that firm.'
   , {'entities': []})
, ('In 2005, our Compensation Committee approved the 2005 Advanced Micro Devices, Inc. Long-Term Incentive Plan (2005 LTIP). This plan became effective on January 1, 2005 and replaced the former long-term incentive plan (Former LTIP) applicable to officers.'
   , {'entities': []})
, ('The Audit Committee meets with Ernst & Young LLP several times a year. The Audit Committee reviews both audit and non-audit services performed by Ernst & Young LLP and the fees charged for such services. Among other things, the Audit Committee examines the effect that the performance of non-audit services may have upon the independence of the registered public accounting firm. All audit-related services and tax services were pre-approved by the Audit Committee after review of each of the services proposed for approval.'
 , {'entities': []})
, ('For fiscal year 2006, Mr. Margolin, an executive officer of the Company, received an annual base salary of approximately $232,000, which was approved by senior management of the Company. Mr. Margolin’s annual and long-term incentive compensation were approved by the Board’s independent Compensation Committee. For fiscal year 2007, all compensation for all executive officers of the Company has been approved by the Board’s independent Compensation Committee.'
   ,  {'entities': []})
, ('he Compensation Committee of the Board (“Committee”) approves all compensation for our named executive officers and authorizes all equity awards under the Advance Auto Parts Long-Term Incentive Plan. Decisions regarding non-equity compensation of other employees are made by management. The Chief Executive Officer annually reviews the performance of each named executive officer and other selected officers. The conclusions reached and recommendations based on these reviews, including with respect to salary adjustments and annual incentive amounts, are presented to the Committee. The Chief Executive Officer’s performance is reviewed annually by the Committee. The Committee has final approval on the determination of compensation recommendations for executives. Management is responsible for developing and maintaining an effective compensation program throughout the Company and preparing documents required for compliance with applicable United States law.'
   , {'entities': []})
, ('Based on the foregoing objectives, the Committee has structured the Company’s annual and long-term incentives to motivate executives to achieve the business goals set by the Company and reward the executives for achieving such goals. The Committee has engaged HayGroup, an independent consulting firm, to conduct an annual review of the total compensation program and to provide relevant market data and alternatives for the Committee to consider when making compensation decisions for our named executive officers, as well as for other key executives.'
   , {'entities': [(260,268, 'CC')]})
, ('Except for the employee stock options awarded in 2006 or awarded as part of the compensation arrangement for a newly hired executive officer, stock option grants have been approved by the Committee at a meeting held one to two days prior to the public release of the Company’s periodic financial results. The grant date for such stock awards is generally the third trading day on New York Stock Exchange following the release of earnings. The grant dates for the February 2006 option grants coincided with the date of approval by the Committee. All options granted in 2006 have a term of seven years and vest in equal thirds during the three years following grant, starting with the first anniversary of the grant, according to the terms of the option agreements. Newly-hired executives are generally eligible to receive long-term incentive grants shortly after their hire date based on guidelines and grant schedule approved by the Committee. Please refer to the “Grants of Plan-Based Awards” and “Outstanding Equity Awards at Fiscal Year-End” tables for additional information about executives’ 2006 long-term incentive awards.For 2007, the Compensation Committee decided to grant long-term incentive awards in the form of stock appreciation rights and restricted stock. The February 2007 long-term incentive awards were granted with 75% of the value in stock appreciation rights and the remaining 25% in restricted stock. Stock appreciation rights were granted with an exercise price equal to the closing stock price on the grant date. Stock appreciation rights have a term of seven years and vest in equal thirds during the three years following grant, starting with the first anniversary of the grant, according to the terms of the stock appreciation rights award certificate. The restricted stock awards do not vest until February 2010, but dividend and voting rights were granted as part of the restricted stock awards.'
   , {'entities': []}) 
, ('The Company provides named executive officers and certain other executives taxable allowances that the Company and the Committee believe are reasonable and consistent with the objectives of the overall compensation program, and better enable the Company to attract and retain superior employees for key positions. The Committee periodically reviews allowance levels for named executive officers. Executives may apply their allowances toward personal automobile expenses, legal and financial planning, health club memberships, and personal supplemental disability or life insurance policies based on their individual needs. The Company specifically excludes country club memberships from its allowance plan. Offering these allowances enables the Company to maintain a competitive total compensation package for executives. Allowance reimbursement amounts for named executive officers are included in the “Summary Compensation Table” contained in this proxy statement. Our named executive officers are also eligible for personal use of the Company airplane in accordance with the airplane use policy approved by the Compensation Committee.'
   , {'entities': []})
,('The Committee has engaged Frederic W. Cook & Co., Inc. (“Cook”), an independent consulting firm, to provide advice and assistance to the Committee when making compensation decisions for our named executive officers, as well as for other senior executives.  Cook reports directly to the Committee, and all services provided by Cook are provided on behalf of the Committee.'  
  , {'entities': [(26,54, 'CC'), (57,61,'CC') , (257,261,'CC'), (326,330,'CC')]})
, ('Cook does not provide any non-executive compensation services to the Company directly or indirectly through affiliates.  In 2009, Cook did not provide any services to the Company other than those requested by the Committee Chair and related to Cook’s engagement as independent consultant to the Committee.'
   , {'entities': [(0,4, 'CC'), (130,134,'CC') , (244,248,'CC')]})
, ('Due to the number of companies comprising the retail compensation data provided by Hay Group, the manner in which these data have been adjusted, and the additional factors taken into consideration in determining the compensation for each executive, we believe describing the retail compensation data in summary form better serves our investors’ understanding of our compensation policies than listing the more than ninety companies in the database.'
   , {'entities': [(83,92, 'CC')]})
, ('The Committee considered compensation data provided by Hay Group based on its 2007 National Retail Industry database as one component of its decisions for executives’ compensation in 2007.  Hay Group collected data from a broad group of over ninety retail companies with which we compete for key management and executive talent.'
   , {'entities': [(55,64, 'CC'), (190,199,'CC')]})
, ('For 2009, the Committee established base salary, annual incentive opportunities, and long-term incentive target grants for our named executive officers primarily with reference to the peer group data provided by Cook.  The Hay Group retail compensation data was used as a secondary reference point.  Generally, the target annual cash compensation (base salary plus target annual incentive compensation) for our named executive officers is approximately at the median level of the peer group.  Executives have the potential to earn significantly higher actual annual cash compensation when our performance significantly exceeds performance goals, or significantly lower actual annual cash compensation if our performance falls short of performance goals.  Long-term incentive target levels for our named executive officers are set at the median of the peer group, with the potential for executive officers to earn higher values at roughly the 75th percentile when performance goals are exceeded over a defined performance period.  Long-term incentive award values will be lower than the median if Company performance goals are not achieved.'
   , {'entities': [(212,216, 'CC'), (223,232,'CC')]})
, ('In 2009, on behalf of the Committee, Cook conducted an annual competitive review of the compensation practices among the peer companies, including named executive officer pay levels and compensation mix.  Cook also reviewed the aggregate long-term incentive grant practices of our peer companies, including potential share dilution from equity compensation grants, annual share usage, and annual fair value transfer costs.'
   , {'entities': [(37,41, 'CC'), (205,209,'CC')]})
, ('The Compensation Committee established an aggregate target bonus pool for payments under the Management Bonus Plan in a manner that would provide plan participants with a target bonus that was designed to be competitive with the composite median bonus paid by the comparison peer group and survey companies. The Compensation Committee further established that the bonus pool would be funded at 90% of target bonus for achievement of the EPS Target, with an additional 10% of target bonus funded for achievement of the Revenue Target and 10% of target bonus funded for achievement of the R&D Reinvestment Target. As a result, 110% of the target bonus would be funded upon achieving all three of the pre-established corporate performance objectives. For any bonus to be payable under the Management Bonus Plan for 2006 performance, 2006 adjusted earnings per share had to be greater than 95.86% of the EPS Target. The Compensation Committee also retained the discretion to reduce any bonus amounts payable to a plan participant based on any factors deemed relevant by the Compensation Committee. As a result of our achievement of 101.2% of our EPS Target, 110.3% of our Revenue Target and 100.3% of our R&D Reinvestment Target, and in accordance with the bonus structure approved at the beginning of 2006, the Compensation Committee approved funding the 2006 bonus pool for plan participants at approximately 133.3% of the target bonus pool. As a result, the Compensation Committee approved a total Management Bonus Plan pool of approximately $30.0 million for approximately 767 participating employees.'
   , {'entities': []})
,('Upon funding, the Compensation Committee considers and approves the allocation of the Management Bonus Plan pool to our business units and business functions (and the executive officers responsible for those business units and business functions) based on each unit’s respective operating income results compared to budgeted amounts and each function’s attainment of specific objectives. For instance, a business unit that performed above budgeted operating income typically receives a greater share of the Management Bonus Plan pool than a business unit that was below the operating income budget. The Compensation Committee also typically uses the business unit and business function allocations in its consideration of bonuses to the named executive officer participants based on the performance of each executive’s business unit or business function. For 2006, the Compensation Committee determined that our business units and business functions (and the executive officers responsible for those business units and business functions) would receive allocations ranging from slightly below to slightly above the 133.3% target bonus pool based on each unit’s and function’s performance separate from our corporate financial performance.'
  , {'entities': []})
, ('Therefore, our Chief Executive Officer had the opportunity to earn a bonus of up to 192% of his year-end annualized base salary, and our President had the opportunity to earn a bonus of up to 112% of his year-end annualized base salary, each based on our performance and subject to the discretion of the Compensation Committee to reduce the amount payable. Similar to the Management Bonus Plan, bonuses for 2006 under the Executive Bonus Plan were paid in cash up to a maximum bonus pool of 100% of the bonus targets, and the remainder was paid in shares of restricted stock which vests (and is subject to forfeiture prior to vesting) in full on the second anniversary of the grant date, subject to continued employment with us through such vesting date. Vesting, however, is accelerated on such date as the participant is eligible for Normal Retirement (having reached the age of 55 and five 5 years of service) or in the event of termination due to death or permanent disability. Vesting is prorated in the case of a job elimination as a result of a reduction in force based on the length of the participant’s service subsequent to the grant date. The restricted stock for 2006 performance was granted on February 2, 2007, under our 1989 Incentive Compensation Plan, as amended. Based upon our relative achievement of the pre-established performance objectives for 2006 and the individual contributions of our Chief Executive.'
   , {'entities': []})
, ('The Compensation Committee targets long-term incentive compensation awards for our named executive officers and other members of our senior management at the 75th percentile of the comparison peer group and survey companies with respect to long-term incentives. In addition, the Compensation Committee reviewed the rate of share usage for equity awards, which represented approximately 2 million shares, or 1.5% of the common shares outstanding, and a three year average rate of share usage of 1.7% of the common shares outstanding, which was at the 40th percentile for our peer group. Under our 1989 Incentive Compensation Plan, as amended, the aggregate number of shares that may be issued pursuant to awards granted during any calendar year is up to 1.5% of our common shares outstanding plus any unused shares available from prior years and shares issued or issuable under awards that again become available for grant (such as upon the termination or expiration of an award). Our 1989 Incentive Compensation Plan, as amended, was approved by our stockholders in 1989 and 2000. The “evergreen” feature of the 1989 Incentive Compensation Plan, as amended, will terminate in connection with the termination of our plan in April 2009. '
   , {'entities': []})
, ('During 2006, the Compensation Committee delegated to Mr. Pyott, our Chief Executive Officer, and Mr. Schaeffer, the Compensation Committee chairperson, the authority to grant stock options with respect to approximately 186,000 shares to former Inamed employees. The Inamed acquisition was completed on March 23, 2006 and the grants were made on April 3, 2006. Mr. Pyott and Mr. Schaeffer were granted full discretion to determine the grant amounts to be made to each individual. In addition, during 2006, Mr. Pyott was authorized to award stock options exercisable for up to 403,000 shares and up to 100,000 shares of restricted stock to current high performing employees and key new hires, in each case who are not executive officers.'
   , {'entities': []})
, ('The Compensation Committee annually reviews our executive officers’ stock ownership status and the timeline for compliance. As of December 31, 2006, all such officers met the stock ownership guidelines. The Compensation Committee also annually reviews, with the help of the independent consultant, our stock ownership guidelines and their consistency with market practices.'
   , {'entities': []})
, ('Earnings on amounts contributed to the 401(k) plan and the retirement contribution feature of the plan are based on participant selection among the investment options selected by an investment subcommittee of our Executive Committee. Participants may select one or more investment options, however, matching contributions are initially invested in our common stock but may be immediately diversified by the participant. In addition, participants who have reached age 55 may elect to self-direct the initial investment of matching contributions to other investment options. No “above-market” crediting rates are offered under either feature of the plan.'
   , {'entities': []})
, ('Mr. Gallagher is a member of and past Chairman of the Board of Advisors of the Haas School of Business, University of California, Berkeley. Mr. Gallagher was elected to our Board in 1998, is Chairman of the Corporate Governance and Compliance Committee, Chairman of the Organization and Compensation Committee and serves as our Board’s lead independent director'
   , {'entities': []})
, ('Mr. Lavigne serves on the board of Accuray Incorporated, a publicly-traded company specializing in the design, development and sale of the CyberKnife System, an image-guided robotic radiosurgery system used for the treatment of solid tumors, and is Chairman of the Board and serves on its Organization and Compensation Committee. He also serves on the board and Audit Committee of Depomed, Inc., a publicly-traded specialty pharmaceutical company focused on treating pain and other central nervous system conditions. Mr. Lavigne also serves on the boards of and is the Chairman of the Audit Committee for DocuSign, Inc., a privately-held digital transaction management company, SafeNet Inc., a privately-held computer security company, and Novocure Limited, a privately-held oncology company. Mr. Lavigne is a board member of Children’s Hospital Oakland, where he serves as Chairman of the Board of the Hospital and Foundation at the Children’s Enterprise Executive Council with the University of California, San Francisco and is a member of the Audit Committee. Mr. Lavigne is a faculty member of the Babson College Executive Education’s Bio-Pharma: Mastering the Business of Science program. Mr. Lavigne is also a Trustee of Babson College and Babson Global. Mr. Lavigne is a former member of the board and Chairman of the Audit Committees of Arena Pharmaceuticals, BMC Software, Inc., Equinix, Inc. and Kyphon, Inc. Mr. Lavigne is also a former Trustee of the California Institute of Technology and the Seven Hills School. Mr. Lavigne was appointed to our Board in July 2005 and is a member of the Audit and Finance Committee and the Science & Technology Committee'
   , {'entities': []})
, ('Mr. Proctor is a member of the several notable legal associations, including the American Bar Association, Association of Corporate Counsel and the International Bar Association. Mr. Proctor has previously served on the boards of Wachovia Corporation and Northwestern Mutual Life and on the charitable boards for the Association of Corporate Counsel, CARE USA, Duke Law School, and the North Carolina Symphony Orchestra. Mr. Proctor was appointed to our Board in February 2013 and is a member of the Audit and Finance Committee and the Organization and Compensation Committee.'
   , {'entities': []})
, ('Mr. Termeer is Chairman of the Board of Aveo Pharmaceuticals, a publicly-traded cancer therapeutics company, and a member of the boards of ABIOMED Inc., a publicly-traded medical device company, Verastem, Inc., a publicly-traded biopharmaceutical company, Medical Simulation Corporation, a privately-held healthcare industry consulting service provider and Moderna Therapeutics, a privately-held biotechnology company. Mr. Termeer is a director of Massachusetts General Hospital, a board member of Partners HealthCare and a member of the board of fellows of Harvard Medical School. Mr. Termeer is also a member of the board of the Massachusetts Institute of Technology and serves on its Executive Committee, is a board member of the Biotechnology Industry Organization, the Life Sciences Foundation, WGBH and Boston Ballet. He is Chairman Emeritus of the New England Healthcare Institute, a nonprofit, applied research health policy organization he was instrumental in founding. Mr. Termeer was a former member of the board of the Federal Reserve Bank of Boston from 2007 to 2011 and its chairman from 2010 to 2011, and a former member of the board of Pharmaceutical Research and Manufacturers of America. In 2010, Mr. Termeer was inducted into the Academy of Distinguished Entrepreneurs, which was established by Babson College to recognize the economic and social contributions of business pioneers. Mr. Termeer received the Pharmaceuticals and Biotechnology Lifetime Achievement Award from Frost and Sullivan in 2009, and was selected by Ernst & Young for its Master Entrepreneur Award in 2007 for the role he has played in guiding the overall development of the biotech industry. Mr. Termeer has also been inducted as a Fellow in the American Academy of Arts and Sciences and was elected in 2005 to Honorary Fellowship at the British Royal College of Physicians. Mr. Termeer was appointed to our Board in January 2014, is a member of the Corporate Governance and Compliance Committee and the Organization and Compensation Committee'
   , {'entities': []})
, ('Frederic W. Cook & Co., Inc. (“Cook & Co.”) was engaged for 2013 as the compensation consultant for the Compensation Committee. The Compensation Committee has taken great care to ensure that the advice provided by its external compensation consultant is objective and unbiased.'
   , {'entities': [(0,28, 'CC'), (31,41,'CC')]})
, ('Cook & Co. performs no work for us other than its work providing executive compensation consulting services to the Compensation Committee and reports directly to the Compensation Committee through its chairperson. In addition, Cook & Co. annually provides a certification to the Compensation Committee regarding its independence and provision of services.'
   , {'entities': [(0,10, 'CC'), (227,237,'CC')]})
, ('PETER J. MCDONNELL, M.D., 54, has served as the Director and William Holland Wilmer Professor of the Wilmer Eye Institute of the Johns Hopkins University School of Medicine since 2003, where he leads the Wilmer Eye Institute, the largest academic ophthalmology department in the country. Dr. McDonnell has also served as the Chief Medical Editor of Ophthalmology Times since 2004, and has served on the editorial boards of numerous ophthalmology journals. He served as a consultant to the United States Department of Health and Human Services in 1996 and also served as the Assistant Chief of Service at the Wilmer Institute from 1987 to 1988.'
   , {'entities': []})
, ('Specifically, the Compensation Committee and Mercer operated under an engagement letter that set forth the terms of the compensation consultant’s engagement, its direct reporting relationship to the Compensation Committee, the ability of the Compensation Committee to replace the compensation consultant at any time and without reason, the services to be provided by the compensation consultant and its fees.'
   ,{'entities': [(45,51, 'CC')]})
, ('In 2009, to ensure that there was further separation between the Compensation Committee’s executive compensation consultant and any consultant used by management for other services, the Compensation Committee retained Frederick W. Cook & Co. as its compensation consultant for 2010.'
   , {'entities': [(218,241, 'CC')]})
,('Cook & Co. has agreed to provide only executive compensation consulting services to the Compensation Committee and will not provide any other services to us.'
  , {'entities': [(0,10, 'CC')]})
, ('Art Levinson has served as the Chief Executive Officer of Calico, a research and development company, since September 2013. Previously, Dr. Levinson served as the Chairman of Genentech, Inc. from September 1999 to September 2014 and as a director and member of the Remuneration Committee of F. Hoffman-La Roche Ltd. from March 2010 to September 2014. Dr. Levinson also served as Chief Executive Officer of Genentech from July 1995 to April 2009, and, from May 2009 to September 2013, served as an advisor to Genentech’s Research and Early Development center and as a member of Genentech’s external advisory group, the Scientific Resource Board. Dr. Levinson previously served as a director of NGM Biopharmaceuticals, Inc. and as Chairman of the Board of Amyris, Inc. Dr. Levinson also serves on the board of directors of the Broad Institute of Harvard and MIT, on the Board of Scientific Consultants of the Memorial Sloan-Kettering Cancer Center, on the Industrial Advisory Board of the California Institute for Quantitative Biomedical Research, on the Advisory Council for the Princeton University Department of Molecular Biology, on the Advisory Council for the Lewis-Sigler Institute for Integrative Genomics, and on the Innovation Advisory Board of the United States Commerce Department. Among other qualifications, Dr. Levinson brings to the Board executive leadership experience, including his service as a chairman of a large public company, along with extensive financial expertise and brand marketing experience.'
   , {'entities': []})   
, ('Ron Sugar is the retired Chairman of the Board and Chief Executive Officer of Northrop Grumman Corporation, a global security company. Dr. Sugar served in this role from 2003 until 2010 and served as President and Chief Operating Officer from 2001 until 2003. He was President and Chief Operating Officer of Litton Industries, Inc. from 2000 until the company was acquired by Northrop Grumman in 2001. He was earlier Chief Financial Officer of TRW Inc. Dr. Sugar serves as the Lead Director of Chevron Corporation, where he has served on the board of directors since April 2005. Dr. Sugar has also been a director of Air Lease Corporation since April 2010, where he is the Chair of the Compensation Committee and a member of the Governance Committee, and of Amgen Inc. since July 2010, where he is the Chair of the Corporate Responsibility and Compliance Committee and a member of the Governance and Nominating Committee. Dr. Sugar also serves as a senior advisor to Ares Management, LLC, Bain & Company, Temasek Americas Advisory Panel and the G100 Network and the World 50, and as a member of the National Academy of Engineering, a trustee of the University of Southern California, a director of the Los Angeles Philharmonic Association, and a national trustee of the Boys and Girls Clubs of America. Among other qualifications, Dr. Sugar brings to the Board executive leadership experience as a chairman and chief executive officer of a large international public company, financial expertise as a former chief financial officer, understanding of advanced technology, and a global business perspective from his service on other boards.'
   , {'entities': []})                
, ('Sue Wagner has served as a director of BlackRock, Inc., an asset management company, since October 2012, where she serves on the Risk Committee. Ms. Wagner was a co-founder of BlackRock and previously served as Vice Chairman from 2006 and as a member of BlackRock’s Global Executive Committee and Global Operating Committee until her retirement in July 2012. During her tenure at BlackRock, she also led strategy and corporate development and the alternative investments and international client businesses. Since April 2014, Ms. Wagner has also served as a director on the boards of Swiss Re Ltd. and Swiss Reinsurance Company Ltd., and from March 2015 has served on the boards of Swiss Re Corporate Solutions Ltd. and Swiss Re Life Capital Ltd. Ms. Wagner serves as the Chair of the Investment Committee and as a member of the Finance and Risk Committee and the Chairman’s and Governance Committee of each Swiss Re company. Ms. Wagner also serves on the boards of DSP BlackRock Investment Managers Pvt. Ltd., Wellesley College, and the Hackley School. Among other qualifications, Ms. Wagner brings to the Board operational experience, including her service as chief operating officer of a large international public company, along with extensive financial expertise and experience in the financial services industry.'
   , {'entities': []})
, ('Gold and Stone serve on the Audit Committee; Ms. Agather (Chairperson) and Messrs. Anderson, Gold, Steinberg and Stone serve on the Compensation Committee; and Messrs. Steinberg and Stone (Chairman) serve on the Nominating and Corporate Governance Committee.'
   , {'entities': []})
, ('We completed a compensation analysis, primarily in 2005, and we retained Ernst & Young (“E&Y”) to assist with planning and evaluation of long-term incentives. Based on the analysis completed by E&Y as well as the analysis completed by our internal Compensation Department, we implemented a short term incentive plan and adjusted the types of equity awarded in 2006 from stock options to restricted stock units and stock settled stock appreciation rights.'
   ,{'entities': [(73,86, 'CC'),(89,92, 'CC'), (194,197,'CC')]} )
, ('Our CEO, other members of management (particularly the Vice President of Human Resources), and Compensation Committee members regularly discuss our compensation issues and the performance and retention of our Named Executive Officers. Mr. Kartsotis, in connection with the Vice President of Human Resources, typically recommends to the Compensation Committee the annual base salary, bonus and equity awards (if any) for the other members of the executive management team, for the Compensation Committee’s review, modification and approval.'
   , {'entities': []})
, ('The Compensation Committee would typically establish the base salary, bonus and equity incentive awards for the CEO, Mr. Kosta N. Kartsotis. However, Mr. Kartsotis refused all forms of compensation for fiscal 2006. Mr. Kartsotis is one of the initial investors in our Company and expressed his belief that his primary compensation is met by continuing to drive stock price growth.'
   , {'entities': []})
, ('The Board of Directors has established three standing committees: the Audit Committee, the Compensation Committee and the Nominating and Corporate Governance Committee. Ms. Agather and Messrs. Anderson (Chairman), Gold and Stone serve on the Audit Committee; Ms. Agather (Chairperson) and Messrs. Anderson, Gold, Steinberg and Stone serve on the Compensation Committee; and Messrs. Steinberg and Stone (Chairman) serve on the Nominating and Corporate Governance Committee.'
   , {'entities': []})
, ("The CEO bases his award grant recommendations for Named Executive Officers each year on a number of factors, including each Named Executive Officer's role, responsibilities and contributions to our business. In recommending the size, frequency and type of long-term incentive grants, the CEO may also take into account tax implications to the individual and to the Company as well as the expected accounting impact and dilution effects. In fiscal 2007, the Compensation Committee considered benchmark data provided by Ernst and Young as well as the Human Resources Department in determining overall award sizes."
   , {'entities': [(518,533, 'CC')]})
, ('Our Compensation Committee consists of Messrs. Barnholt,     Bourguignon, Kagle, and Tierney. Mr. Kagle was the chairman     of the committee until April 1, 2006, when     Mr. Barnholt became the chairman of the committee.     Mr. Ford was a member of the committee until April 1,     2006, when he moved to the Corporate Governance and Nominating     Committee. The committee met 12 times during 2006. The     Compensation Committee reviews and'
   , {'entities': []})
, ('Our Compensation Committee consists of Messrs. Barnholt,     Bourguignon, Ford, Kagle, and Tierney. Mr. Ford joined the     committee on March 27, 2008. Mr. Barnholt is the     chairman of the committee. The committee met 10 times during     2007. The Compensation Committee reviews and approves all     compensation programs applicable to directors and executive     officers, the overall strategy for employee compensation, and     the compensation of our CEO and our other executive officers.     The committee also reviews the Compensation Discussion and     Analysis contained in our proxy statement and prepares the     Compensation Committee Report for inclusion in our proxy     statement. All members of our Compensation Committee are     independent under the listing standards of the Nasdaq Global     Select Market. The Compensation Committee Charter permits the     committee to, in its discretion, delegate all or a portion of     its duties and responsibilities to a subcommittee of the     committee. You can view our Compensation Committee Charter on     the corporate governance section of our investor relations     website at '
   , {'entities': []})
, ('Mr. Henry WK Chow was appointed to the Committee in May 2011.'
   , {'entities': []})
, ('Fifty percent (50%) of the performance bonus is payable upon our achievement of the pre-established "target" levels for the two semi-annual performance periods (i.e., January 1, 2012 to June 30, 2012 and July 1, 2012 to December 29, 2012) of the following performance measures approved by the Compensation Committee under the EIP: non-GAAP net income, non-GAAP gross margin and revenue; 25% of the performance bonus is payable upon the achievement by the SeaMicro business, a company we recently acquired, of certain subjective integration objectives; and 25% of the performance bonus is payable upon her (i) successful integration of product marketing and select engineering teams for graphics, semi-custom, and server businesses by the end of 2012, (ii) successful staffing of key managerial positions in her division, and (iii) ability to work across company functions to structure responsibilities and collaborate with our engineering, sales, marketing and operations functions, in each case, as subjectively determined by Mr. Read and the Compensation Committee for the performance period ended December 29, 2012.'
   , {'entities': []})
, ('The Compensation Committee currently consists of Mr. Caldwell, as Chair, Ms. Denzel and Mr. Donofrio, each determined to be "independent" under applicable SEC and Nasdaq rules.'
   , {'entities': []})
, ("Mr. Ghilardi is key to promoting AMD's future growth and profitability, and as a result thereof, the Compensation Committee subjectively increased his base salary to appropriately reflect proportional pay between Messrs. Ghilardi and Meyer."
   , {'entities': []})
, ( 'Fifty percent (50%) of the performance bonus is payable upon our achievement of the pre-established "target" levels for the two semi-annual performance periods (i.e., January 1, 2012 to June 30, 2012 and July 1, 2012 to December 29, 2012) of the following performance measures approved by the Compensation Committee under the EIP: non-GAAP net income, non-GAAP gross margin and revenue; 25% of the performance bonus is payable upon the achievement by the SeaMicro business, a company we recently acquired, of certain subjective integration objectives; and 25% of the performance bonus is payable upon her (i) successful integration of product marketing and select engineering teams for graphics, semi-custom, and server businesses by the end of 2012, (ii) successful staffing of key managerial positions in her division, and (iii) ability to work across company functions to structure responsibilities and collaborate with our engineering, sales, marketing and operations functions, in each case, as subjectively determined by Mr. Read and the Compensation Committee for the performance period ended December 29, 2012.'
   , {'entities': []})
, ( "Fifty-percent of any PRSUs earned pursuant to the attainment of a CAGR performance level will vest and be paid out upon the Compensation Committee's certification of attainment of the CAGR performance level (provided, however, that no PRSUs may be earned or vest prior to August 16, 2016, one year from the grant date) and the remaining 50% will vest and be paid out at the end of the Performance Period, subject in each case to the Named Executive Officer's continued employment through each such vesting date, unless his or her employment agreement or other agreement with us provides otherwise."
   , {'entities': []})
, ("In fiscal 2015, the Board and Compensation Committee reviewed competitive market data regarding non-employee directors' pay compiled by Compensia, Inc., the Compensation Committee's independent compensation consultant."
   , {'entities': [(136,151, 'CC')]})
, ('The Compensation Committee currently consists of Mr. Caldwell, as Chair, Ms. Denzel and Mr. Donofrio, each determined to be "independent" under applicable SEC and Nasdaq rules.'
   ,  {'entities': []})
, ('Independent Compensation Consultant'
   ,{'entities': []})
, ('In setting these amounts, the Leadership Development and Compensation Committee also considered aggregated market information from third party surveys including compensation data for retail, internet and technology companies including Adobe Systems, AOL, Best Buy, BMC Software, Cisco, Dell, eBay, Gap, IBM, Intel, Intuit, Microsoft, Oracle, Sun, Target and Yahoo.'
   , {'entities': []})
, ('The Plan provides that, unless our Compensation Committee determines otherwise at the time of grant with respect to a particular award, in the event of a “change in control,” (i) any unvested options and stock appreciation rights outstanding as of the date the change in control is determined to have occurred will become fully exercisable and vested; provided, however, that the Committee may determine to cancel each option or SAR for a payment in an amount equal to the difference between the price paid in the change in control transaction and the purchase price per share under the option or SAR; (ii)'
   , {'entities': []})
, ('The employment agreements with Messrs. Jackson, Norona, Sherman and Tyson provide that any incentive compensation granted to the executive by us is subject to our Incentive Compensation Clawback Policy as adopted by our Board or the Compensation Committee from time to time.'
   , {'entities': []})
, ('For Mr.       Jackson, the definition of “Good Reason” includes failure of the       Nominating Committee of the Board'
   , {'entities': []})
, ('The Board may grant Awards to Independent Directors, subject to the limitations of the Plan, pursuant to a written non-discretionary formula established by the Committee, or any successor committee thereto carrying out its responsibilities on the date of grant of any such Award (the "Independent Director Equity Compensation Policy").'
   , {'entities': []})
, ('The Independent Director Equity Compensation Policy shall set forth the type of Award(s) to be granted to Independent Directors, the number of shares of Stock to be subject to Independent Director Awards, the conditions on which such Awards shall be granted, become exercisable and/ or payable and expire, and such other terms and conditions as the Committee (or such other successor committee as described above) shall determine in its discretion.'
   , {'entities': []})
, ('As defined in the letter agreement, retirement means termination of full time employment with Fossil, Inc. and our subsidiaries and related companies on the date set forth in a written retirement notice addressed to our Chief Executive Officer and our Compensation Committee and delivered to our General Counsel no later than one year prior to his retirement date.'
   , {'entities': []})
, ('For 2010, upon recommendation of the Compensation Committee, the Board of Directors has adopted, subject to stockholder approval, the Fossil, Inc. 2010 Cash Incentive Plan.'
   , {'entities': []})
, ("The total amount of fees the Company paid F.W. Cook in 2007 was $111,207, which included the fees paid for services provided as the independent compensation consultant to the HRC and GNC, reimbursement of F.W. Cook's reasonable travel and business expenses, and a fee of less than $5,000 for a survey of long-term incentives which is used for benchmarking for other positions throughout Wells Fargo."
   , {'entities': [(42,51, 'CC'), (205,214,'CC')]})
, ('In addition, notwithstanding anything to the contrary herein, the Committee may grant Shorter Vesting Awards as determined by the Committee and evidenced in an Award Agreement provided that the aggregate number of Shares underlying all such Shorter Vesting Awards granted under the Plan shall not exceed 24,159,766 Shares, as adjusted pursuant to Section 26.'
   , {'entities': []})
, ("Mr. Gutierrez         served as Vice Chair of Albright Stonebridge Group from April 2013 to         February 2014; Vice Chairman of the Institutional Clients Group at         Citigroup Inc. from January 2011 to February 2013; a consultant at the         Global Political Strategies division of APCO Worldwide Inc., a         communications and public affairs consulting firm, from December 2009 to         April 2013; Chairman of the Global Political Strategies division of APCO         Worldwide Inc. from January 2010 to January 2011; the 35th U.S.         Secretary of Commerce from February 2005 to January 2009; Kellogg         Company's Chairman of the Board (from April 2000 to February 2005),         Chief Executive Officer (from April 1999 to February 2005) and President         (from 1998 to September 2003); and in various executive and         non-executive positions at Kellogg Company from 1975 to         1998."
   , {'entities': []})
, ('Mr. Parsons (Chairman and CEO during 2007), Mr. Bewkes (President and COO during 2007), Ms. Fili-Krushel (Executive Vice President, Administration) and Mr. Mark Wainger (Senior Vice President, Global Compensation and Benefits) reviewed these self-assessments before they were presented to the Committee.'
  , {'entities': []})
, ('The Committee has retained John England, Managing Principal of Towers Perrin, as its independent executive compensation consultant since 2002.'
  , {'entities': [(27,40, 'CC'), (63,76,'CC')]})
, ("In     April 2008 Ursula O. Fairbairn, Chairman of the Compensation     Committee, was selected by the Board to serve as presiding     director until VF's 2009 Annual Meeting of Shareholders."
   , {'entities': []})
, ('The current members of the compensation committee are William S. Shanahan (Chairperson), Thomas J. Campbell, Suzanne Nora Johnson, and John A. Swainson, each of whom has been determined by our board to be independent under applicable stock exchange rules.'
   , {'entities': []})
, ('The Committee removed Sun Microsystems Inc. from the peer group because it was acquired by Oracle and removed HSBC North America because it is a division of a larger global company and therefore compensation data for the division is not publicly available.'
   , {'entities': []})
, ('Notwithstanding the foregoing provisions of this Section 7.8 to the contrary, the Committee may determine in its discretion that a SAR may be exercised following any such Termination, whether or not exercisable at the time of such Termination; provided, however, that in no event may a SAR be exercised after the expiration date of such SAR specified in the applicable Award Agreement, except as provided in the last sentence of Section 6.5 (in the case of Tandem SARs) or in the last sentence of Section 7.4 (in the case of Freestanding SARs).'
   , {'entities': []})
, ('In addition to our independent Chair, the board has three standing committees: the Audit and Risk Committee, chaired by Mary B. Cranston; the Compensation Committee, chaired by Suzanne Nora Johnson; and the Nominating and Corporate Governance Committee, chaired by Alfred F. Kelly.'
   , {'entities': []})
, ("(a)      Notwithstanding any provision of the Plan to the contrary, the Committee shall have the authority to determine (and may so provide in any Agreement) that a Participant's (including his or her estate's, beneficiary's or transferee's) rights (including the right to exercise any Option or SAR), payments and benefits with respect to any Award shall be subject to reduction, cancellation, forfeiture or recoupment (to the extent permitted by applicable law) in the event of the Participant's Termination for Cause or due to voluntary resignation; serious misconduct; violation of the Company's or a Subsidiary's or Affiliate's policies; breach of fiduciary duty; unauthorized disclosure of any trade secret or confidential information of the Company or a Subsidiary or Affiliate; breach of applicable non-competition, non-solicitation, confidentiality or other restrictive covenants; or other conduct or activity that is in competition with the business of the Company or any Subsidiary or Affiliate, or otherwise detrimental to the business, reputation or interests of the Company and/or any Subsidiary or Affiliate; or upon the occurrence of certain events specified in the applicable Award Agreement (in any such case, whether or not the Participant is then an Employee, Non-Employee Director or Consultant)."
   , {'entities': []})
, ('For compensation purposes, EPS from continuing operations, Adjusted FCF, and operating income are adjusted to exclude the effects of events that the Compensation Committee deems do not reflect the performance of the named executive officers.'
   , {'entities': []})
, ("The Audit Committee has recommended the ratification of Deloitte & Touche LLP as the Company's independent registered public accounting firm for purposes of United States securities law reporting for the year ending September 30, 2011."
   , {'entities': []})
, ('        Going forward, the Committee expects to continue to review and refine this group with input from its new independent compensation consultant, Farient Advisors LLC ("Farient"). '
   , {'entities': [(150,170, 'CC'), (173,180,'CC')]})
, ("        In carrying out its role in establishing executive compensation plans, the Committee receives advice from an independent compensation consultant, and considers pay strategies and recommendations prepared by the Company's management. Under its charter, the Committee has the sole authority to retain, compensate and terminate the independent compensation consultants and any other advisors necessary to assist it in its evaluation of director, CEO or other senior executive compensation. In connection with the Separation, the Committee reevaluated its independent compensation consultant and, after reviewing the qualifications of several consultants, determined that Farient was best positioned to provide the Committee with independent advice going forward."
   , {'entities': [(676,683,'CC')]})
, ( "        The Audit Committee is responsible for the annual retention of our independent registered public accounting firm, subject to shareholder approval at the Annual General Meeting. The Audit Committee is directly responsible for the appointment, compensation, oversight and evaluation of performance of the work of the external auditors. The Audit Committee has recommended the ratification of Deloitte & Touche LLP as the Company's independent registered public accounting firm for purposes of United States securities law reporting for the year ending September 27, 2013. "
   , {'entities': []})
, ("        The Audit Committee is responsible for the annual retention of our independent registered public accounting firm, subject to shareholder approval at the Annual General Meeting. The Audit Committee is directly responsible for the appointment, compensation, oversight and evaluation of performance of the work of the external auditors. The Audit Committee has recommended the ratification of Deloitte & Touche LLP as the Company's independent registered public accounting firm for purposes of United States securities law reporting for the year ending September 27, 2013. "
   , {'entities': []})
, ('Farient does not provide any additional work to the company and satisfies NYSE consultant independence standards. '
   , {'entities': [(0,7,'CC')]})
, ('The committee concluded that Kwan does not violate any NYSE consultant indepdendence standards.'
   , {'entities': [(29,33,'CC')]})
, ('6a. to elect Deloitte AG (Zürich) as statutory auditors until the next annual general meeting; 6b. to ratify appointment of Deloitte & Touche LLP as independent registered public accounting firm for purposes of United States securities law reporting for the year ending September 26, 2014;'
   , {'entities': []})
, ('The Compensation Committee of the Board of Directors is composed of Robert H. Hotz, Leatrice Ducat, Robert A. Meister and John F. Williams, Jr.,'
   , {'entities': []})
, ('The members of the Compensation Committee are Leatrice Ducat, Robert H. Hotz, Robert A. Meister and John F. Williams, Jr.,'
   , {'entities': []})
, ('(In previous years, when we did not have an Executive     Chairman, the Committee would approve all grants of equity-based     compensation to the CEO and COO, and all executives reporting to     either the CEO or COO.)'
   , {'entities': []})
, ('Messrs. Correll, Hughes, Minor and Prince comprised the     entire Compensation Committee during all of 2006.'
   , {'entities': []})
, ('Also, the Committee has the discretion to revise payouts under MIP based on individual performance.'
   , {'entities': []})
, ('Executive compensation under LTIP is crucial to the success of the firm.'
   , {'entities': []})
, ('This review is described in greater detail under the caption, "2009 Risk Adjusted Pay for Performance Review" in the Compensation Committee Report which follows this CD&A.'
   , {'entities': []})
, ('As a result of the passage of EESA and our participation in the CPP, the Committee strengthened this recoupment policy.'
   , {'entities': []})
, ('As a result of the passage of TARP and our participation in the CPP, the Committee strengthened this recoupment policy in 2009.'
   , {'entities': []})
, ('In order to provide retirement benefits at levels comparable to those intended by the current plan, the Committee approved including a portion of salary shares equivalent to the target MIP award for compensation purposes under the SERP.'
   , {'entities': []})
, ('Since salary shares were not contemplated at the time this plan was designed, the Committee decided to include a portion of the salary shares equivalent to the target MIP award for purposes of the ERISA Excess Plan Personal Pension Account.'
   , {'entities': []})
, ('The Committee amended the 2009 Stock Plan, the MIP, and most other incentive compensation plans to include a provision which contractually implements this.'
   , {'entities': []})
, ('Messrs. Correll, Crowe, Garrett, Hughes, Linnenbringer, and Ratcliffe, and Dr. Wynn constitute all of the directors who served on our Compensation Committee at any time during'
   , {'entities': []})
, ('In broad terms, our compensation programs for executive officers, which are reviewed by our independent Compensation Committee and its advisor, Semler Brossy Consulting Group, LLC (SBCG), focus on performance-based criteria and reflect the competitive environment in which we operate.'
   , {'entities': [(144,179,'CC')]})
, ('In specifying the performance goals applicable to any performance period, the Committee may provide that one or more objectively determinable adjustments shall be made to the performance measures on which the performance goals are based, which may include adjustments that would cause such measures to be considered "non-GAAP financial measures" within the meaning of Rule 101 under Regulation G promulgated by the Securities and Exchange Commission.'
   , {'entities': []} )
, ('In fiscal 2011, the Compensation Committee took the following notable actions related to LTI grants for our NEOs:'
   , {'entities': []})
, ('The Compensation Committee conducted a comprehensive review of all pay elements, including perquisites, as part of its outreach efforts following the 2013 Say on Pay vote.'
   , {'entities': []})
, ('In specifying the performance goals applicable to any performance period, the                                          Committee may provide that one or more objectively determinable adjustments shall be                                          made to the performance measures on which the performance goals are based, which may                                          include adjustments that would cause such measures to be considered “non-GAAP financial                                          measures” within the meaning of Rule 101 under Regulation G promulgated by the                                          Securities and Exchange Commission.'
   , {'entities': []} )
, ('Messrs. Johnson and Stumpf rotated off of the Compensation Committee following the preparation of this report.'
   , {'entities': []})
, ('In 2008, management recommended, and the Compensation Committee approved, amendments to Sunoco\'s Executive Incentive Plan, or EIP, and the Long-Term Performance Enhancement Plan II, or LTPEP II, to incorporate a "clawback" policy with regard to the annual incentive and long-term incentive equity awards in the case of a financial restatement that was the result of employee misconduct, or in the case of fraud, embezzlement or other serious misconduct that was materially detrimental to Sunoco.'
   , {'entities': []})
, ('The Management Committee also performs an annual compensation risk assessment of all the non-executive compensation plans, at both the parent and subsidiary levels (excluding Sunoco Logistics Partners L.P.).'
   , {'entities': []})
, ('In March 2011, the Committee adopted a policy that, unless required by law, prohibits Staples from entering into any future compensation, severance or employment related agreement that provides for a gross up payment to cover taxes triggered by a change in control, including taxes payable under Section 280G of the U.S. Internal Revenue Code.'
   ,{'entities': []} )
, ('In March 2013, the Committee set compensation for the NEOs based on its December 2012 review of 2009-2011 compensation, its assessment of our 2012 performance, stockholder feedback and results of 2012 Say on Pay advisory vote, and general consideration of the totality of the data, advice, and information provided by management and Exequity.'
   , {'entities': [(333,341,'CC')]})
, ("In 2015, management engaged its own compensation consultant, Willis Towers Watson, separately from the Committee's compensation consultant, to help develop the CEO's recommendations to the Committee."
   , {'entities': [(61,81, 'CC')]})
, ("After the end of each fiscal year, the Compensation Committee     reviews management's recommendations for MIP bonuses (other     than a recommendation for the Co-CEOs for whom management makes     no recommendation)."
   , {'entities': []})
, ('The Compensation Committee evaluates the     following criteria and information in approving MIP awards for     executive officers:'
   , {'entities': []})
, ('The J. M. Smucker Company Executive     Compensation Committee Charter'
   , {'entities': []})
, ('She is also a director, and a member     of the compensation committee, of Steelcase Inc., a furniture     and office systems manufacturer, and Belk, Inc., a large,     privately owned department store chain in the United States.'
   , {'entities': []})
, ('Perrin Survey and Mercer Survey and for all non-durable goods     companies from the Watson Wyatt Survey is used when the     Compensation Committee reviews compensation.'
   , {'entities': [(0,6, 'CC'), (18,24,'CC'), (85,97,'CC')]})
, ('On May 1, 2013, the Compensation Committee also approved special one-time grants of restricted shares to the following Named Executive Officers: 10,000 shares granted to Mark R. Belgya, which shares vest at the end of the five-year period from the date of grant; 10,000 shares to Vincent C. Byrd, which shares vest at the end of the three-year period from the date of grant; and 10,000 shares to Steven Oakland, which shares vest at the end of the five-year period from the date of grant.'
   , {'entities': []})
,('The members of our Compensation Committee during fiscal year     2007 were Messrs. Davidson, Reyes and Thompson.'
  , {'entities': []} )
, ('To the extent permitted under Section 162(m)(4)(C) of the Code, and the regulations promulgated thereunder, such performance targets may be established in writing by the Compensation Committee not later than 90 days after the commencement of the period of service to which the performance targets relate, provided that the outcome is substantially uncertain at the time the Compensation Committee actually establishes the performance targets; and provided, further, that in no event shall the performance targets be established after 25% of the period of service (as scheduled in good faith at the time the performance targets are established) has elapsed.'
   , {'entities': []})
, ('With respect to any bonus award that qualifies as "performance-based compensation," within the meaning of Section 162(m)(4)(C) of the Code, any of the performance targets described in Section 2.1, if applicable to such bonus award, shall be established in writing by the Committee not later than 90 days after the commencement of the period of service to which the performance targets relate, provided that the outcome is substantially uncertain at the time the Committee actually establishes the performance targets; and provided, further, that in no event shall the performance targets be established after 25% of the period of service (as scheduled in good faith at the time the performance targets are established) has elapsed.'
   , {'entities': []})
, ('The members of our Compensation Committee during fiscal year 2009 were Messrs. Thompson, Kiernan, Reyes, Marquardt (until October 30, 2008) and Zander (beginning on April 29, 2009).'
   , {'entities': []})
, ('On January 29, 2009, the Compensation Committee adopted the Pay Recovery Policy, which provides standards for recovering compensation from an Executive where such compensation was based on incorrectly reported financial results due to the fraud or willful misconduct of such Executive.'
   , {'entities': []})
, ("In general, the Compensation Committee, in consultation with F.W. Cook and the independent members of the Board, determines each element of the CEO's compensation."
   ,  {'entities': [(61,70,'CC')]})
, ('Fifty percent of the annual Board and committee retainer is deferred in a notional account that replicates the Common Stock Fund under the Prudential Employee Savings Plan ("PESP").'
   , {'entities': []})
, ('Please see "Consideration of Last year\'s \x91Say on Pay\' Vote" in the CD&A for a discussion of how our Board and the Compensation Committee responded to the results of last year\'s advisory vote.'
   , {'entities': []})
, ('After careful consideration, and given the extensive changes we made in the past, the Committee did not make any changes to our executive compensation program and policies as a result of the most recent Say on Pay advisory vote.'
   , {'entities': []})
, ('The Audit and Finance Committee has selected Ernst & Young LLP as our independent registered public accounting firm for fiscal year 2016 and has further directed that management submit the selection of the independent registered public accounting firm for ratification by our stockholders at the annual meeting.',
  {'entities': []} )
, ('The Audit Committee has appointed, and, as a matter of good corporate governance, is requesting ratification by the shareholders of the appointment of, the registered public accounting firm of Ernst & Young LLP ("E&Y") to serve as independent auditors for the fiscal year ending December 31, 2014.'
   , {'entities': []})
, ('Accordingly, the Audit and Finance Committee has appointed Ernst & Young LLP ("E&Y") to perform audit and other permissible non-audit services for the Company and its subsidiaries.'
   , {'entities': []})
, ('For all of the other NEOs, the Compensation Committee adopted the Executive Severance Plan and sent notices to each of Messrs. Partridge, Pollitt, Floum and Sheedy that their current employment agreements would not be renewed beyond the scheduled expiration dates in March 2011 or May 2011 in the case of Mr. Sheedy.'
   , {'entities': []})
, ('The members of our Compensation Committee during fiscal year 2008 were Messrs. Thompson, Reyes, Marquardt and James A. Davidson.'
   , {'entities': []})
, ('Each year, the Compensation Committee adjusts the payment scale to align to goals communicated to investors for ROE and, since 2005, growth in EPS.'
   , {'entities': []})
,('The following directors served on the Compensation and Management Development Committee at December 31, 2007: Thomas D. Bell, Jr., Charles R. Crisp, Michael J. Durham, Arthur E. Johnson (Chair), James A. Rubright and Bettina M. Whyte.'
  , {'entities': []})
,('You may designate a proxy other than the proxy committee by striking out the name(s) of the proxy committee and inserting the name(s) of your chosen representative(s).'
  , {'entities': []})
,('As of December 31, 2006, the members of the Committee were Vance D. Coffman, Robert S. Morrison, Aulana L. Peters, Rozanne L. Ridgway, and Kevin W. Sharer.'
  , {'entities': []})
, ('During 2006, the Committee was assisted by its independent compensation consultant, George B. Paulin of Frederic W. Cook & Co., Inc.'
   , {'entities': [(84,100, 'CC'), (104,132,'CC')]})
, ('The compensation committee, whose members are W. J. Farrell, chairman, H. L. Fuller, E. M. Liddy, and W. A. Osborn, held two meetings in 2011.'
   , {'entities': []})
, ('In particular, this CD&A explains how the Compensation Committee (the "Committee") and Board of Directors made its compensation decisions for the Company\'s executives, including the five named officers: Miles D. White, Chairman of the Board and Chief Executive Officer; Thomas C. Freyman, Executive Vice President, Finance & Chief Financial Officer; Hubert L. Allen, Executive Vice President, General Counsel and Secretary; Richard W. Ashley, Executive Vice President, Corporate Development; and Brian J. Blaser, Executive Vice President, Diagnostics Products.'
   , {'entities': []})
,('Each of Messrs. Burman, Martinez and Perrin, who are currently directors of the Company, and each of Ms. Brooks, Ms. Gallagher and Mrs. Shern, who are new director nominees, was recommended to the Nominating and Board Governance Committee by Spencer Stuart.'
  , {'entities': []})
, ('These restricted share units vest on March 31, 2016, subject to Mr. Tippl’s continued employment through such date, as follows: (a) approximately 45% (i.e., a maximum of 154,959) vest if the Compensation Committee determines that the non-GAAP diluted earnings per share objective set forth in our 2015 AOP has been met or exceeded; (b) approximately 27% (i.e., a maximum of 92,975) vest if the Compensation Committee determines that the adjusted non-GAAP free cash flow objective set forth in our 2015 AOP has been met or exceeded; and (c) approximately 27% (i.e., a maximum of 92,975) vest if the Compensation Committee determines that the adjusted non-GAAP operating income objective for Blizzard Entertainment set forth in our 2015 AOP has been met or exceeded.'
   , {'entities': []})
, ('These stock options and restricted share units vest on July 28, 2016, subject to Mr. Kelly’s continued employment through such date, in each case if the Compensation Committee determines that the non-GAAP diluted earnings per share objective set forth in our 2015 AOP has been met or exceeded.'
   , {'entities': []})
, ('That is, if our adjusted 2015 non-GAAP operating income was at least 75% of the adjusted non-GAAP operating income target for the year set forth in the annual operating plan approved by our Board for that year (such plan for any given year, the “AOP”), the bonus to be paid to each executive would be $10,000,000 less the amount of any other “senior executive plan bonus” within the meaning of the 2014 Plan that was paid or to be paid to that person for 2015, and subject to the Compensation Committee’s use of negative discretion to reduce or eliminate that bonus.'
   , {'entities': []})
, ('subject to his execution of an effective and irrevocable release, a lump-sum payment of $1,360,000 for each of 2016, 2017 and 2018, if his employment was terminated after December 31st of the respective year and the Compensation Committee determines that Activision Publishing’s adjusted non-GAAP operating income for that year is both (1) positive (i.e., $1 or greater) and (2) 85% or more than the adjusted non-GAAP operating income objective for Activision Publishing set forth in the AOP for that year,'
   , {'entities': []})
, ('Since we exceeded the threshold level of 85% of the adjusted non-GAAP operating income target for the year set forth in the 2015 AOP, each of our named executive officers was eligible to receive a bonus of $10,000,000 for 2015, subject to the Compensation Committee’s use of negative discretion to reduce or eliminate that bonus.'
   , {'entities': []})
, ('In 2013, the Committee again engaged an independent outside executive compensation consulting firm, Thomas E. Shea & Associates, LLC ("Shea & Associates"), to assist the Committee with compensation matters.'
   , {'entities': [(100,132, 'CC'), (135,152,'CC')]})
, ('Shea & Associates, which provides no other services to us, reported its findings directly to the Committee.'
   , {'entities': [(0,17,'CC')]})
, ('Shea & Associates, which provides no other services to us, reported its findings directly to the Committee.'
   ,{'entities': [(0,17,'CC')]})
, ('In setting executive officer compensation levels, the Committee considered the comparative compensation analyses provided by Shea & Associates, and then applied the collective experience and judgment of the Committee to such data (and the relative significance of the various comparative universe components) to make compensation determinations.'
   ,{'entities': [(125,142,'CC')]})
, ('A representative of Shea & Associates met with the Committee in formal Committee meetings, as well as outside Committee meetings in sessions with Committee members, particularly with the Committee Chair, at key points throughout the year to update the Committee on the status of compensation surveys, and make recommendations regarding executive officer and director compensation programs and levels.'
   , {'entities': [(20,37,'CC')]})
, ('The Audit Committee of the Board of Directors is composed of Robert L. Wright (Chairman), Douglas W. Johnson (financial expert), Charles B. Knapp, and Marvin R. Schuster, each of whom qualifies as an independent Director under the NYSE listing standards.'
   , {'entities': []})
, ('The Audit Committee of the Company’s Board of Directors is composed of four Directors, each of whom, the Board has determined, is independent as defined by the NYSE listing standards and SEC rules, and is financially literate. The Board has determined that at least one member of the Audit Committee is an audit committee financial expert as defined by the SEC rules. Mr. Douglas W. Johnson, with 30 years as an auditor with Ernst & Young, 20 of those years as a partner, working primarily with the insurance industry segment, is the audit committee financial expert. The Audit Committee operates under a written charter adopted by the Board of Directors.'
   , {'entities': []})
, ('Typically, Committee meetings are attended by, for all or a portion of each meeting, not only the Committee members but also our Chief Executive Officer, our Vice President of Human Resources, an independent compensation consultant from Compensia, Inc. and legal counsel from Fenwick West LLP.'
   , {'entities': []})
, ('For fiscal year 2010, the Executive Compensation Committee, with input from Compensia, management and our Chief Executive Officer, determined the level of equity compensation opportunity for each of our NEOs based upon data from the peer group (as adjusted by Compensia, as described above), and, to a lesser degree, the other factors for determining compensation discussed under "Executive Summary\x97Total Rewards Program for our NEOs\x97Competitive Positioning" above.'
   , {'entities': []})
, ('Adobe and the Executive Compensation Committee value the input of our stockholders on our Total Rewards Program.'
   , {'entities': []})
, ('In view of this outcome, as well as the feedback that we gathered through our engagement efforts with many of our stockholders prior to our 2011 Annual Meeting of Stockholders about our executive compensation practices, the Executive Compensation Committee decided to redesign several significant aspects of our Total Rewards Program, including as it pertains to our executive officers.'
   , {'entities': []})
, ('The Compensation Committee reviews base salary, bonuses, profit sharing contributions, and grants of Stock Options, RSUs, PUs, PSUs, retirement and other compensation for our Officers and for such other employees as the Board may designate.'
   , {'entities': []})
, ("Mr. Cassidy's almost 40 years of experience in the power generation industry in various positions of increasing responsibility with PSEG provide him with strong insight, particularly with regard to power operations, power sector strategy, management and corporate governance matters, and make him a qualified member of our Board and effective Chairman of our Compensation Committee."
   , {'entities': []})
,('Applying this methodology, the consultant suggested adding five companies to the Peer Group (Chesapeake Energy Corporation, EOG Resources, Inc., Noble Energy, Inc., PPL Corporation and Questar Corporation).'
  , {'entities': []})
,("Consistent with our guiding principles, the desired market percentiles serve as guideposts for the Committee's thinking rather than strict policy for establishing compensation."
  , {'entities': []})
, ('The Committee also established a series of performance targets based on our income before income taxes (“PTI”) for fiscal 2013 (excluding the effect of acquisitions, divestitures and accounting changes) corresponding to award payouts ranging from 50% to 150% of the target awards.'
   , {'entities': []})
, ('The members of the Compensation Committee of the Board of Directors during fiscal 2015 were Timothy D. Cook, Elizabeth J. Comstock, John C. Lechleiter, and Johnathan A. Rodgers.'
   , {'entities': []})
,('Consistent with prior years, 2012 PEPunit and LTC Awards were approved by the Compensation Committee at its regularly-scheduled meeting in February.'
  , {'entities': []})
,("RadioShack's compensation and benefits department, which directly reports to James F. Gooch, RadioShack's Chief Financial Officer, utilizes analyses and data to assist the MD&C Committee in determining the types and amounts of compensation elements to be paid to the named executive officers (other than the CEO)."
  , {'entities': []})
,('The Compensation Committee is currently comprised of three non-employee directors: James F. Orr III, Committee Chairman, Christine Cournoyer and Frank R. Mori.'
  , {'entities': []})
,('Consistent with the requirement in our Compensation Committee charter, the Committee annually reviews the independence of its compensation consultant considering the factors set forth in the New York Stock Exchange listing standards.'
  , {'entities': []})
, ('Consistent with past practice, the committee adjusted the reported results on which certain 2012 EPIP measures were determined to eliminate the effects of certain items.'
   , {'entities': []})
,('We have a Compensation Committee currently composed of Christopher W. Bodine, Christopher J. Coughlin and Ronald R. Taylor.'
  , {'entities': []})
, ('We have a Nominating and Corporate Governance Committee currently composed of Christopher W. Bodine, James H. Bloem, Christopher J. Coughlin, Catherine M. Klema, Ronald R. Taylor and Fred G. Weiss.'
   , {'entities': []})
, ('Consistent with these results, the Executive Compensation Committee determined that, based on strong ARR in our Digital Media business and new business bookings (“NBB”) in our Digital Marketing business, as well as achievement of key customer advocacy objectives, the annual cash incentive awards for our NEOs were paid out at 116% of their target award opportunity (for more discussion of cash awards, see section captioned “Cash Incentives” below).'
   , {'entities': []})
, ('The members of the Governance and Compensation Committee are James W. Hovey, Paula A. Sneed, David M. Stout and Lee M. Thomas.'
   , {'entities': []})
, ('James G. Brocksmith, Jr., age 66, has served as a director of Alberto-Culver since October 2002 and as an independent business consultant for more than the past five years.'
   , {'entities': []})
, ('The Organization and Compensation Committee (the "Compensation Committee") is currently composed of Mr. Schaeffer (chairperson), Messrs. Ingram, Gallagher and Ray and Ms. Hudson.'
   , {'entities': []})
, ("Ms. Hudson is a director of Lowe's Companies, Inc., a publicly-traded nationwide chain of home improvement superstores, where she serves on the Compensation Committee and the Governance Committee, P.F. Chang's China Bistro, Inc., a publicly-traded national Asian dining restaurant chain, where she serves on the Compensation and Executive Development Committee and the Nominating and Corporate Governance Committee, and Interpublic Group of Companies, a publicly-traded company, one of the world's leading organizations of advertising agencies and marketing services companies."
   , {'entities': []})
, ('Nolan Lehmann served at the Chairman of the Compensation Committee during 2007 and until February 2008, when James Quella became the Chairman of the Compensation Committee.'
   , {'entities': []})
, ('This award further recognized that the Compensation Committee and the Board of Directors asked Mr. Camilleri to assume the role of Chairman and Chief Executive Officer of PMI, while accepting a reduction in his compensation at PMI.'
   , {'entities': []})
, ('The current members of the Committee are: Thomas F. Farrell II (Chair); Elizabeth E. Bailey; Gerald L. Baliles; Robert E. R. Huntley; and Thomas W. Jones.'
   , {'entities': []})
, ('Mr. Webb is a director of Triad Financial Corporation,     Hilltop Holdings Inc., a publicly traded holding company that     anticipates seeking to make strategic acquisitions and     investments and that currently owns a property and casualty     insurance operation where he serves on the compensation     committee, M & F Worldwide Corp., a holding company     that manages two financial institution services companies and a     licorice flavorings manufacturer, where he serves on the audit     committee, and is a former director of Plum Creek Timber     Company, where he served on the audit and compensation     committees.'
   , {'entities': []})
, ('For the cycle commencing on January 1, 2011 and ending on December 31, 2013, with the assistance and advice of Towers Watson, the compensation and human resources committee of US Airways Group established TSR rankings in comparison to the following publicly traded airlines:'
   , {'entities': []})
, ("The Committee's Consideration of the 2011 Nonbinding Advisory Vote to Approve the Compensation of Our Named Executive Officers"
   , {'entities': []})
, ('In December 2012, the Compensation Committee approved amendments to our incentive cash compensation plans (EIP, GMIP and VEP) to expressly allow the Compensation Committee, or management, as appropriate, to consider employee misconduct that caused serious financial or reputational damage to the Company when determining whether an employee has earned an annual cash incentive award or the amount of any such award.'
   , {'entities': []})
, ('Mr. Bohen is also a director of the Polish American Freedom     Foundation and chairman of its investment committee, a director     and treasurer of the TEAK Fellowship, a not-for-profit     organization that mentors and assists gifted adolescent children     from disadvantaged circumstances, and non-executive chairman of     the board of The Fund for Teachers, a Texas non-profit     corporation.'
   , {'entities': []})
, ('Prior to joining the Company, she was consultant/principal of     MMH Consulting Services, a privately-held human resources     consulting firm, from 2006 to September 2007, executive vice     president and senior vice president - human resources with Texas     Genco LLC, a wholesale power generator, from 2005 to 2006, and     senior vice president - human resources and administration     of Integrated Electrical Services, Inc., from 2000 to 2005.'
   , {'entities': []})
, ('Currently, Mr. Joung is a consultant for TPH Asset Management, LLC, an affiliate of Tudor, Pickering, Holt & Co.'
   , {'entities': []})
, ('The Committee has engaged Aon Consulting, which, together with James G. Purvis, Executive Vice President of Human Resources, and his executive compensation team, supports the Committee in its work.'
   , {'entities': []})
, ("The Compensation Committee determined Mr. Considine's     STI by the extent to which Aimco met five designated corporate     goals, which are described below and are referred to as     Aimco's Key Performance Indicators, or KPI."
   , {'entities': []})
, ('George A. Zimmer has been a director of Apollo Group since June 2006 and served as a member of the Compensation Committee of the Board of Directors of Apollo Group during the 2007 fiscal year.'
   , {'entities': []})
, ("During the portion of the 2007 fiscal year from November 14, 2006 to June 15, 2007, Mr. D'Amico was employed by FTI Palladium Partners and served as Chief Financial Officer in a consultant capacity pursuant to a service contract between the Company and FTI."
   , {'entities': []})
, ("The Compensation Committee determined Mr. Considine's     STI by the extent to which Aimco met five designated corporate     goals, which are described below and are referred to as     Aimco's Key Performance Indicators, or KPI."
   , {'entities': []})
, ("The amount reported in this column does not include any similar housing allowance or reimbursed travel expenses which Mr. D'Amico received from FTI Palladium Partners during the period he served as a consultant to the Company pursuant to the service contract between the Company and FTI Palladium Partners."
   , {'entities': []})
, ('Prior to June 15, 2007, he provided services to the Company as the Chief Financial Officer in a consultant capacity pursuant to a service contract between the Company and FTI Palladium Partners.'
   , {'entities': []} )
, ("During fiscal 2009, the following directors were members of Applied's Human Resources and Compensation Committee: Aart J. de Geus, Thomas J. Iannotti, Willem P. Roelandts (Chair) and James E. Rogers."
   , {'entities': []})
, ("The Committee's principal contact was Ira T. Kay, who departed from Towers Watson in 2010, initially to an independent advisory firm called Ira T. Kay & Company, subsequently merged into Pay Governance LLC."
   , {'entities': []})
, ('During 2009, the Nominating and Corporate Governance Committee engaged an outside consulting firm, ClearBridge Compensation Group LLC, to provide a study on director compensation.'
   , {'entities': []})
, ('The Compensation Committee is currently composed of John D.     Forsyth (Chair), Walter E. Boomer, Carole J. Shapazian and     Thomas T. Stallkamp.'
   , {'entities': []} )
, ('The directors who constituted the Compensation Committee during some or all of 2014 were Anna R. Cablik, John P. Howe III, M.D., Tollie W. Rich, Jr. and Edwin H. Welch,'
   , {'entities': []})
, ('PBRSU and RSU awards that were approved by the Compensation Committee on Sunday, February 22, 2015 had a grant date of Monday, February 23, 2015, the first trading day following the date of the approval.'
   , {'entities': []})
, ('The Audit Committee has appointed Deloitte & Touche LLP, an independent registered public accounting firm, to serve as our independent auditor for 2016.'
   , {'entities': []})
, ('During our last completed fiscal year, the voting members of our Compensation Committee were Jere A. Drummond, Chairman, Jan Carlson, Vicki L. Sato and Thomas T. Stallkamp.'
   , {'entities': []})
, ("The Committee received input from, among others, Messrs. Zuckerman, D. Linde and Norville on the various members of the senior management team; in addition both the Committee and SMG had access to each officer's self-assessment of his performance against pre-established goals."
   , {'entities': []})
, ("He has also been a member of the Financial     Accounting Standards Board Advisory Council, the Public Company     Accounting Oversight Board's Standing Advisory Group, the     AICPA's Special Committee on Financial Reporting, the     AICPA's SEC Practice Section Executive Committee and     the AICPA's Ethics Executive Committee."
   , {'entities': []})
, ('Termination for "Good Reason" in Mr. Ratner\'s employment agreement means that (1) without Mr. Ratner\'s consent, (A) his base salary or bonus target as an employee is reduced, (B) prior to December 31, 2014, the aggregate target value of his awards (as determined in good faith by the Compensation Committee at the time of grant and including the anticipated annual award amount increase under his outstanding deferred compensation award with respect to the year) under the long-term cash or equity programs and arrangements of the Company is less than $1.4 million, unless such reduction in value is in proportion to the reduction in the aggregate target values of the awards granted for such year to all of named executive officers listed in the Company\'s proxy statement relating to the immediately preceding year that are still full-time executive officers at the time of such reduction, (C) the Company requires that his principal office be located outside of Nassau County or Manhattan, (D) the Company materially breaches its obligations to Mr. Ratner under the employment agreement, (E) he is no longer the Vice Chairman of the Company, (F) he reports directly to someone other than the Chairman of the Board of Directors of the Company or, provided that James L. Dolan is the Chief Executive Officer of the Company, the Chief Executive Officer of the Company, (G) his responsibilities immediately after the effective date of the employment agreement are thereafter materially diminished, or (H) if (i) prior to December 31, 2014, his employment with MSG is terminated by MSG without "Cause" or by him for "Good Reason" (as Cause and Good Reason are defined in his MSG employment agreement), (ii) he has been unable to find a position with another company that (a) is comparable in responsibility, stature and compensation to his position at MSG and (b) would accommodate his continuing responsibilities at the Company under this Agreement, despite a good faith effort to find such a position over the 30-day period following such termination of his employment with MSG and he provides prompt notice thereof to the Company and'
   , {'entities': []})
, ("Mr. Cassidy's almost 40 years of experience in the power generation industry in various positions of increasing responsibility with PSEG provide him with strong insight, particularly with regard to power operations, power sector strategy, management and corporate governance matters, and make him a qualified member of our Board and effective Chairman of our Compensation Committee."
   , {'entities': []})
, ("The Compensation Committee's current members are Rodman L. Drake (Chairman), Michael D. Casey and James J. Loughlin (since June 2008)."
   , {'entities': []})
, ('Prior to joining PepsiCo, Mr. Kellogg was a senior consultant with Arthur Andersen & Co. and Booz Allen & Hamilton.'
   , {'entities': []})
,('Subsequently, the Compensation Committee approved salary increases for Messrs. Buchi, Groenhuysen and Aragues as a result of their February 2010 promotions to Chief Operating Officer, Chief Financial Officer and Executive Vice President, respectively.'
  , {'entities': []})
, ('Messrs. Cash, Claflin, and Gallagher and Ms. O’Brien, who comprised the Compensation Committee as of the end of'
   , {'entities': []})
, ('Based on the recommendation of the Governance, Compensation and Nominating Committee, the Board has nominated the following current Class II Directors for election: Ralph W. Babb, Jr., James F. Cordes and Jacqueline P. Kane.'
   , {'entities': []})
, ('For 2015, the Compensation Committee has decided to (i) remove the airline companies (Alaska Air Group Inc., JetBlue Airways Corp., Republic Airways Holdings Inc., and SkyWest Inc.) in order to narrow the business focus of the peer group, (ii) add four companies that have grown to reflect the peer group characteristics discussed above (ArcBest Corporation, Hub Group, Inc., Kansas City Southern and Old Dominion Freight Line, Inc.), and (iii) remove Werner Enterprises Inc. to avoid overweighting smaller companies.'
   , {'entities': []})
, ('For Mr. Krull, whose position is not reported as consistently in proxy data, the Compensation Committee considered only the survey data, with equal weighting between the Mercer and Equilar surveys.'
   ,{'entities': [(170,176, 'CC'), (181,188,'CC')]})
, ("For fiscal 2013, the Compensation Committee set each named executive officer's base salary as follows: William Dillard, II\x97$1,000,000, Alex Dillard\x97$970,000, Mike Dillard\x97$695,000, Drue Matheny\x97$695,000 and James I. Freeman\x97$750,000."
   , {'entities': []})
, ("Simpson Thacher reviewed and advised the Committee on the form and the terms and conditions of the employment agreements with Messrs. Hunter, Doyle, Churchill and Pontual, and, for Mr. White's employment agreement, on behalf of the Committee, drafted and negotiated the terms and conditions with Mr. White's attorney, but had no material role in determining the forms or level of compensation for any of the agreements."
   , {'entities': []})
, ('Mr. Calbert started his professional career as a consultant with Arthur Andersen Worldwide, where his primary focus was on the retail/consumer industry.'
   , {'entities': []})
, ('Christopher J. Coughlin, age 55, has served as a director of D&B since December 2004, and is a member of the Audit Committee and Compensation & Benefits Committee.'
   , {'entities': []})
, ('In 2008, the Compensation Committee selected Net Cash Generation and Combined Consumer Digital Imaging Group (CDG) and Graphics Communication Group ('
   , {'entities': []})
, ('From 2001 to 2003, Mr. Janitz served as a       consultant with JPMorgan Partners, Kidd Associates, Aurora Capital       Partners, and Questor Management.'
   , {'entities': []})
, ('and Windle B. Priem, who did not stand for re-election at the 2014 Annual Meeting of Shareholders, served on the Leadership and Compensation Committee until April 30, 2014.'
   , {'entities': []})
, ('“Retirement” means for an employee, consultant or advisor of the Company or any of its Subsidiaries, the voluntary retirement by the Participant from service as an employee, consultant or advisor of the Company or any of its Subsidiaries, (a) with respect to Awards granted to the Participant prior to December 9, 2009 (i) after the Participant has attained at least fifty-five years of age and at least five years of continuous service as an employee, consultant or advisor of the Company or any of its Subsidiaries or (ii) after the Participant has attained at least twenty years of continuous service as an employee, consultant or advisor of the Company or any of its Subsidiaries, and (b) with respect to Awards granted to the Participant on or after December 9, 2009, after the Participant has attained at least sixty years of age and at least ten years of continuous service as an employee, consultant or advisor of the Company or any of its Subsidiaries.'
   , {'entities': []})
, ('Mr. Day is also a director of Tidewater, Inc., a publicly traded workboat and compression services provider, where he serves on the Compensation and Nominating and Corporate Governance Committees, and of ONEOK, Inc., the publicly traded general partner of ONEOK Partners, a provider of natural gas gathering, processing, storage and transportation services, where he serves as the Chair of the Executive Compensation Committee and a member of the Executive Committee.'
   , {'entities': []})
, ('Looking to 2011, in 2010 but with effect on January 1, 2011 or shortly thereafter, the Compensation Committee granted each named executive officer options and awards under the 2011 VEP and the 2011 VDA.'
   , {'entities': []})
, ("The Board of Directors has determined that each member of the Audit, Compensation and Nominating & Governance Committees and, with the exception of Frederick W. Smith, each of the Board's members (James L. Barksdale, August A. Busch IV, John A. Edwardson, Judith L. Estrin, J.R. Hyde, III, Philip Greer, Shirley A. Jackson, Steven R. Loranger, Gary W. Loveman, Charles T. Manatt, Joshua I. Smith, Paul S. Walsh and Peter S. Willmott) is independent and meets the applicable independence requirements of the New York Stock Exchange (including the additional requirements for Audit Committee members) and the Board's more stringent standards for determining director independence."
   , {'entities': []})
, ('The current members of the Organization and Compensation Committee are Peter J. Fluor (Chair), James T. Hackett, Kent Kresa, Joseph W. Prueher and Peter S. Watson.'
   , {'entities': []})
, ('James M. Ringler is a member of the Board of Directors and audit committee of The Dow Chemical Company, a vendor of FMC Technologies.'
   , {'entities': []})
, ("In November 2010, the Compensation Committee recommended, and the Board approved, an increase in Mr. della Sala's target award opportunity from 120% to 150% of his base salary payable pursuant to his agreement with FWI, effective October 22, 2010, as compensation for the period during which he serves as our Interim Chief Executive Officer."
   , {'entities': []})
,("In 2007, the Committee retained Hewitt and independent outside counsel to advise the Committee in negotiating new employment contracts with Mr. Dubow, the Company's Chairman, President and Chief Executive Officer, and Gracia C. Martore, the Company's Executive Vice President and Chief Financial Officer."
  ,{'entities': []})
,('Ms. Shalala received director compensation in stock options, including her annual long-term award of an option to purchase 5,000 shares, an option to purchase 1,888 shares granted as payment for Board and committee meetings attended between April 2005 and April 2006, and an option to purchase 3,536 shares granted as payment of her 2006-2007 annual retainer fee.'
  , {'entities': []})
, ("The Board noted that Dr. Jonathan B. Perlin, the Company's Chief Medical Officer and President \x96 Clinical and Physician Services Group, serves on the Board of Directors of Meharry Medical College, but does not serve on the Compensation Committee and is not otherwise involved in determinations related to Dr. Riley's compensation as president and chief executive officer of Meharry Medical College."
   , {'entities': []})
, ('Additionally, the Company retained Marcella K. Arline, our former Chief People Officer who retired from the Company on December 31, 2007, as a consultant to provide compensation advice to the Committee in early 2008 pending the election of a new Chief People Officer.'
   , {'entities': []})
, ('The compensation and management development committee of the     board of directors is composed of Thomas H. Kean, Chairman,     Nicholas F. Brady, Frank A. Olson, Ernst H. von     Metzsch and Robert N. Wilson.'
   , {'entities': []})
, ('The HRC Committee continued to retain Dentons US LLP ("Dentons") as its independent legal counsel.'
   , {'entities': []})
, ('The Committee employs its own independent compensation consultant, Frederic W. Cook & Co., Inc. ("Cook"), as well as its own independent counsel, Sonnenschein Nath & Rosenthal LLP.'
   , {'entities': [(67,95, 'CC'), (98,102,'CC')]})
, ('D.C. He is a member of the board of directors, nominating and corporate governance committee and compensation committee of CoStar Group,'
   , {'entities': []})
, ("The firm's legal counsel is Kwan & Associates, LLC.",
   {'entities': []})
, ('Dr. Forbes is also Professor of Radiology, Mayo Clinic College of Medicine, and Consultant in the Department of Diagnostic Radiology at Mayo Clinic, positions he has held since 1990 and 1977, respectively.'
   , {'entities': []})
, ('On September 22, 2012, the Compensation Committee approved a grant to the newly elected director, Christopher J. Policinski, of a prorated award of 2,250 restricted shares of stock and 3,300 stock options.'
   , {'entities': []})
, ("The current members of the Committee are Kurt J. Hilzinger, Chairman, W. Roy Dunbar, and James J. O'Brien."
   , {'entities': []})
, ("Trizetto Group Inc. The chief executive officer recommended the increase in Mr. Venkata's base salary based on reference to the 50th percentile of the Radford Survey Group and Mr. Venkata's experience and tenure with the Company, which the Compensation Committee supported."
   , {'entities': [(151,158, 'CC')]})
, ("The fact that the value of past equity awards was well below expected levels did not influence the Committee's 2009 executive compensation decisions generally, but it did influence the decision to award RSUs in connection with the new employment agreements for Messrs. Haffner, Flanigan, and Glassman, discussed on page 41."
   ,  {'entities': []})
, ('Mr. Henderson also served as a consultant for AlixPartners LLC, a business consulting firm, from March 2010 until August 2010.'
   , {'entities': []})
, ('Accordingly, the Compensation Committee retained TSR as a modifier to the ROIC performance results for the 2013 performance share awards.'
   , {'entities': []})
,('The Compensation and Organization Development Committee currently consists of Ms. Kropf as Chairman, Dr. Cole, Messrs. Kelson, Kilts and Powers.'
  , {'entities': []})
, ("We do not believe that comparisons to the Expected Proxy Advisory Firm Peer Group are appropriate for us because, according to the Compensation Consultant's analysis, we are not similar in size or market capitalization to the companies in that peer group: our revenues were in the 82nd percentile of the Expected Proxy Advisory Firm Peer Group and our market capitalization was in the 90th percentile."
   , {'entities': []})
, ('In addition, the Board has determined that James I. Cash, Jr., Dina Dublon, and Charles H. Noski are "audit committee financial experts" as defined by Securities and Exchange Commission ("SEC") rules.'
   , {'entities': []})
, ("The law firm of the company is Westhheimer, PLC.",
   {'entities': []})
, ('Extensive experience in the mining business, including both shaft and open-pit; member of the Association of Professional Engineers, Geologist and Geophysicists of Alberta; received the CIM Fellowship award for contributions to the coal industry in Canada; and serves as a consultant to the mining industry with a focus on operational excellence.'
   , {'entities': []})
, ('The     HBB Compensation Committee did expect the ROTCE performance     target for the Frozen HBB Long-Term Plan would be met by HBB in     2007.'
   , {'entities': []})
, ('The Compensation     Committee did expect the ROTCE performance would exceed the     target for the short-term plan at HBB in 2007.'
   , {'entities': []})
, ("To take advantage of Mr. Brady's experience, particularly as a member of our Audit Committee, the Board has asked Mr. Brady to stand for re-election in 2013 for one additional year."
   , {'entities': []})
, ('In this regard, Al Broaddus, a longstanding director, retired in April 2013, and another longstanding director and chair of our Audit Committee, James Brady, will retire at this annual meeting.'
   , {'entities': []})
, ("Accordingly, for measurement of the new company's relative performance in 2011, the compensation committee identified an industrial peer group comprised of the following companies: Global Logistic Properties, Goodman Group, Segro plc, East Group Properties, Inc., First Industrial Realty Trust, Inc., DCT Industrial Trust, and Duke Realty Corporation."
   , {'entities': []})
, ('Mr. Spogli is a trustee of Stanford University and of the J. Paul Getty Trust and a member of the Investment Committee of the California Institute of Technology, a director of Grandpoint Capital Inc., a bank holding company, a member of the Board of Directors of SAVE, S.p.A., which operates the Venice Marco Polo Airport, and of White Bridge Investments, an Italian investment company.'
   , {'entities': []})
, ("RadioShack's compensation and benefits department, which directly reports to James F. Gooch, RadioShack's Chief Financial Officer, utilizes analyses and data to assist the MD&C Committee in determining the types and amounts of compensation elements to be paid to the named executive officers (other than the CEO)."
   , {'entities': []})
, ('Statement by Thomas R. Hix, Chair of the Compensation Committee'
   , {'entities': []})
, ("Fees paid to the Committee's external compensation consultants in fiscal year 2013 were approximately $182,200 to Frederic W. Cook & Co, Inc. and approximately $79,500 to its U.K. associated firm FIT Remuneration Consultants LLP, such fees being charged on the firms' standard terms of business for advice provided."
   ,  {'entities': [(114,141, 'CC'), (196,228,'CC')]})
, ("The Committee also directed Cook & Co. and FIT to assist in the continual development and evaluation of compensation policies, the review of competitive compensation information and the Committee's determinations of compensation levels and awards."
   , {'entities': [(28,38, 'CC'), (43,46,'CC')]})
, ("In fiscal year 2012, the Secondary Executive Committee consisted of Judy Bruner, the Company's Executive Vice President, Administration and Chief Financial Officer, and James F. Brelsford, the Company's Chief Legal Officer and Senior Vice President of IP Licensing."
   , {'entities': []})
, ('The following persons served as members of the Compensation Committee during 2012: John G. Breen, George W. Buckley, Carlos M. Cardoso, Benjamin H. Griswold, IV (Chair), Anthony Luiso and Marianne M. Parrs.'
   , {'entities': []})
, ('Although TSYS is a "controlled" company under the     rules of the NYSE as a result of its 81.1% ownership by Synovus     and CB&T, and as such is entitled to an exemption from the     independence requirements for its Board and its Corporate     Governance and Nominating Committee and Compensation Committee,     TSYS is not currently taking advantage of this exemption.'
   , {'entities': []})
, ('In addition, the Committee engages Frederic W. Cook, & Co., Inc., a nationally-known compensation consulting firm, to provide information regarding compensation levels and practices of peer companies including, specifically, Belo Corp., Clear Channel Communications, Inc., Dow Jones & Company, Inc., Gannett Co., Inc., Hearst-Argyle Television, Inc., IAC/InterActive Corp., The McClatchy Company, McGraw-Hill Companies, Inc., The New York Times Company, The E.W. Scripps Company and The Washington Post Company (the "Peer Group").'
   , {'entities': []})
, ("Pay elements outside the scope of the Committee's annual compensation decisions such as:"
   , {'entities': []} )
, ('In addition, the Committee considered     anticipated unusual items in 2009, including an increase in     pension expense stemming from the sharp decline in global     securities markets in 2008, which was expected to negatively     impact 2009 earnings by about $.50 per share, or more than 8%.'
   , {'entities': []} )
, ('The Committee may also consider information provided by Pay Governance on a broad industry peer group, which, as in fiscal year 2011, was comprised of the following companies in fiscal year 2012: Altria Group, Inc., AT&T Inc., Cablevision Systems Corporation, CBS Corporation, Cisco Systems, Inc., The Coca-Cola Company, Comcast Corporation, Dell, Inc., Gannett Co., Inc., General Electric Company, Hewlett-Packard Company, International Business Machines Corporation, News Corporation, PepsiCo, Inc., The Procter & Gamble Company, Qwest Communications International Inc., Sprint Nextel Corporation, Time Warner Inc., Verizon Communications Inc., The Walt Disney Company and Yahoo!'
  , {'entities': [(56,70,'CC')]})
, ('Currently there are four non-employee members of the Board on the Audit Committee   Christopher C. Davis, Thomas S. Gayner (who was appointed to serve on the Audit Committee in January 2007), George W. Wilson and Richard D. Simmons, who serves as chairman of the Audit Committee.'
   , {'entities': []})
, ('Martore and Whyte and Messrs. Bernlohr, Gellerstedt and Powers are the current members of our compensation committee, and Mr. Gellerstedt is chairman of the compensation committee.'
   , {'entities': []})
, ('Gracia C. Martore, compensation committee member'
   , {'entities': []})
, ('Wok Acquisition Corp. Ms. Anderson serves on the Finance Committee of The Columbus Foundation and as a member of the Board and Chairs the Finance Committee of OhioHealth Corporation.'
   , {'entities': []})
, ('The Compensation Committee currently consists of Michael J. Kneeland (Chairman), Matthew A. Doheny and James E. Hoffman (the "New Compensation Committee").'
   , {'entities': []})
, ('The Compensation Committee currently consists of Michael J. Kneeland (Chairman), Matthew A. Doheny and James E. Hoffman.'
   , {'entities': []})
, ( "The     Committee shall specify the circumstances in which such Awards     shall be paid or forfeited in the event of a Participant's     death, disability or Retirement, in connection with a Change of     Control or, subject to the one-year performance condition set     forth in Sections 6(d)(ii) and (e)(ii), in connection with     any other termination of employment prior to the end of a     performance period or settlement of such Awards."
   , {'entities': []})
, ('The Nominating Committee of the Board consulted various materials regarding current trends and best practices for determining compensation for boards of directors primarily from NACD Blue Ribbon Commission, Pearl Meyer & Partners, and Frederick W. Cook and Co., Inc.'
   , {'entities': [(178,205, 'CC'), (207,229,'CC'), (235,260,'CC')]})
, ( 'From September 1981 to February 2004, Mr. Quella also worked at Mercer Management Consulting and Strategic Planning Associates, its predecessor firm, where he served as a senior consultant to CEOs and senior management teams, and was Co-Vice Chairman with shared responsibility for overall management of the firm.'
   , {'entities': []})
,('LLC, Orient Bay LLC, Ambac Financial Services LLC, and any other entities that the Compensation Committee shall determine.'
  , {'entities': []})
,("In 2011, the Committee also considered materials prepared by Mercer and Johnson Associates related to various aspects of AIG's efforts to comply with the TARP Standards and the requirements of the Special Master."
  , {'entities': [(61,67, 'CC'), (72,90,'CC')]})
,("The Committee noted that the Cook firm reviewed the reports prepared by Johnson Associates prior to consideration by the Committee and determined that this appropriately addressed any conflict of interest raised by Johnson Associates' work or business relationship with AIG."
  , {'entities': [(72,90,'CC')]})
, ( 'For over twenty years, from 1970 to 1991, Mr. Lewis was a strategic management consultant at Boston Consulting, as Founding Chairman of Strategic Planning Associates, and as Chairman of Mercer Management Consulting, a division of Marsh and McLennan.'
   , {'entities': []})
, ('In this regard, for our named executive officers, the Compensation Committee used as a benchmark a survey prepared by Frederic W. Cook & Co., with input from management, regarding compensation levels in 2014, for comparable positions at the following financial services firms: American Equity Investment Life Holding Company, Assured Guaranty Ltd., Employers Holdings, Inc., Horace Mann Educators Corporation, MBIA Insurance Corp., MGIC Investment Corporation, Montpelier Re Holdings Ltd., National Western Life Insurance Company, The Navigators Group, Inc., OneBeacon Insurance Group, Ltd., Platinum Underwriters Holdings, Ltd., Radian Guaranty Inc., Safety Insurance Group, Inc., Selective Insurance Group, Inc., and Virtus Investment Partners,'
   , {'entities': [(118,140,'CC')]})
,("The Committee also determined that Murphy Oil Company should replace Plains Exploration & Production Company since it meets the industry criteria and is the appropriate size, is a peer of the Company's direct peers and is also designated as a peer of Anadarko by various proxy advisors."
  , {'entities': []})
, ('In granting awards to Messrs. Zinsner, Hess, Meaney and Real, the Compensation Committee considered the equity compensation levels of comparable executives at our peer group, as well as the equity already held by each executive.'
   , {'entities': []})
, ('The consultant provides expert advice and guidance on the design and implementation of performance-based compensation programs that align with Company strategy, business and market characteristics, talent requirements, culture, management style and performance and Total Rewards strategies.'
   , {'entities': []})
, ("In approving such award, the Compensation Committee considered the retentive and performance-based nature of the award, Mr. Fradin's significant management responsibility for our Aon Hewitt segment, and the intended purpose of the AHPP, which is to perform as a management integration tool that will align senior leaders from Hewitt with our legacy consulting unit under a common performance-based long-term equity incentive program."
   , {'entities': []})
, ('Mr. Dozer also serves on the boards of directors of Blue Cross Blue Shield of Arizona, where he serves as Chairman of the Finance Committee and a member of the Executive, Audit and Human Resources Committees, and Meridian Bank, where he serves as Chairman of the Governance and Nominating Committee and as'
   , {'entities': []})
, ('As a result of this process, the Audit Committee has selected Deloitte & Touche LLP (??Deloitte??) as the Company??s independent registered public accounting firm and as auditors of the Company??s consolidated financial statements for the fiscal year ending'
   , {'entities': []})
, ('From 2007 to 2011, Mr. McDermut served as managing director and financial consultant at Avant Advisory Group, LLC, a management consulting firm based in Los Angeles and Santa Barbara, CA.'
   , {'entities': []})
, ('He then worked as a principal with William M. Mercer, as a consultant with Tillinghast-Towers Perrin and as Vice President of the Southeast Region for Blue Cross/Blue Shield of Wisconsin prior to rejoining Assurant Health in 1999 as Chief Financial Officer.'
,   {'entities': []} )
, ('His years of service as an executive officer at technology companies, including Intuit and HPLabs, provide him with the executive compensation knowledge necessary to serve on our Compensation and Human Resources Committee.'
   , {'entities': []})
, ('The nominating/corporate governance committee acts under a written charter, which is available online at http://www.adp.com/about-us/governance/nominating-corporate-governance-committee-charter.aspx.'
   , {'entities': []})
, ('The Science and Technology Committee is currently composed of Wayne T. Hockmeyer, Ph.D. (Chair), Uma Chowdhry, Ph.D., James R. Gavin III, M.D., Ph.D. and Carole J. Shapazian.'
   , {'entities': []})
, ('The Governance Committee retained Heidrick & Struggles to conduct a director search in fiscal 2010.'
   , {'entities': []})
, ('Because of the spin-off of BHS, the Compensation Committee amended the 2008 Company EPS measure and the performance measurements attributable to BHS to adjust the time period for which BHS performance targets are included in the measurement period.'
   , {'entities': []})
, ("He also serves as the Chair of FPL Group's Executive       Committee."
   , {'entities': []})
, ( 'The members of the Compensation Committee are Ms. Hackett and Messrs. Shattuck, Gross and Hay.'
   , {'entities': []})
, ( 'Independent adviser to Compensation Committee'
   , {'entities': []})
, ('A majority of the directors of each company and all of the members of the Audit Committee, Compensation Committee, HESS Committee and Nominating & Governance Committee of each company are independent (as defined by the listing standards of the NYSE and the UK Combined Code).'
   , {'entities': []})
, ("For such executives, our Compensation Committee anticipates that it will preliminarily approve the Time Vesting Equity Awards each February (when it also determines the executives' annual performance awards) for such executive's prior fiscal-year performance equal to an amount based on considerations contemplated by the EIP\x97that is, corporate or business unit performance against budgeted financial goals, achievement of non-financial and strategic goals, economic and relative performance considerations and assessments of individual performance."
   , {'entities': []})
, ("age 71; a director since July 1, 2009; President and Chief Executive Officer of Gephardt Group, a multi-disciplined consulting firm, since January 2005; consultant to Goldman Sachs & Co. since January 2005; strategic advisor in the government affairs practice group of DLA Piper between June 2005 and December 2009; senior advisor to FTI Consulting between January 2007 and December 2009; member of the U.S. House of Representatives from 1976 to 2005, representing Missouri's Third District and holding key leadership positions, including House Minority Leader; currently a director of Centene Corporation, Ford Motor Company, Spirit Aerosystems Holdings, Inc. and United States Steel Corporation; formerly a director of Dana Holding Company within the past five years, and a director of Embarq prior to July 1, 2009."
   , {'entities': []})
, ( 'Upon her reelection to the Board of Directors in July 2008, M. Jeannine Strandjord was appointed to the Compensation Committee.'
   , {'entities': []})
, ('Mr. Cook does not receive any   compensation or fees for serving on the Board or any Board committee.'
   , {'entities': []})
, ('In April 2008, the bonus targets for Mr. Mercer,     Mr. Scherp, Mr. Chittipeddi, Ms. Hu and     Mr. Peterson were set by the Compensation Committee in     their respective employment agreements.'
   , {'entities': []})
, ('For over twenty years, from 1970 to 1991, Mr. Lewis was a strategic management consultant at Boston Consulting, as Founding Chairman of Strategic Planning Associates, and as Chairman of Mercer Management Consulting, a division of Marsh and McLennan.'
   , {'entities': []})
, ("He also serves as the Chair of FPL Group's Executive       Committee."
, {'entities': []})
, ( "The Compensation Committee administers the Cliffs' executive compensation program, including compensation for Cliffs' CEO, Joseph A. Carrabba, its CFO, Laurie Brlas and the other three highest paid employees as of December 31, 2009, Donald J. Gallagher, William A. Brake and William R. Calfee."
, {'entities': []})
, ('Similarly, the Human Resources Committee reviewed the performance of Ms. Nichols and Messrs. Blodgett, Lednicky, Cook and Hochberg during the 2008 performance year and their specific contributions in leading their respective functions.'
, {'entities': []})
, ( 'Mr. Cook has served Intuit in various capacities since its founding, serving as CEO and Chairman, and has been the Chairman       of the Executive Committee of the Board of Directors of Intuit since       August 1998.'
, {'entities': []})
, ('In addition, the Committee received base salary, target annual incentive, and target long-term incentive grant value data from the Towers Watson 2011 Energy Services, the Towers Watson 2011 General Industry, and the AonHewitt 2011'
, {'entities': [(131,144, 'CC'), (171,184,'CC'), (216,225,'CC')]})
, ("The compensation committee believes that these vesting schedules make the equity awards more valuable to Facebook in retaining our executive officers and reflect our emphasis on Facebook's long-term success."
, {'entities': []})
, ( 'Independent Business Adviser and Consultant.'
, {'entities': []})
, ("Before approving Mr. Hay's 2006 base pay increase, the Compensation Committee discussed at length such factors as Mr. Hay's individual"
, {'entities': []})
, ('Mr. Richman has been a Consultant to Deloitte Tax, LLP since 2008.'
, {'entities': []})
, ('The Compensation Committee has selected CVA as the sole measure upon which to base our short-term incentive program because it is a key measure on which we set our performance expectations for the year'
, {'entities': []})
, ("the Committee reviewed the 2012 US Mercer Benchmark Database   Executive, as well as Towers Watson's 2012 Executive Compensation Databank."
, {'entities': [(35,41, 'CC'), (85,98,'CC')]})
, ("The Compensation Committee also considered these and other factors in its bonus determinations for the other Named Executive Officers as follows: for Mr. Gallagher, his role in HCP's achieving 4.2% year-over-year growth in same property performance and its strategic investments and dispositions during the year; for Mr. Schoen, his role in HCP's total shareholder return of 14.2% for the year, capital structure management and capital market financings; for Mr. Klaritch, his role in HCP's achieving significant year-over-year growth in same property performance in the medical office building segment, executing significant transactions and leading HCP in its sustainability initiatives that resulted in material energy usage reduction and the receipt of important awards and certifications; and for Mr. Mercer, his role in advising HCP and the Board on strategic business and legal matters, including the structure and negotiations of our transactions, and corporate governance developments."
, {'entities': []})
, ('At the same time, the Compensation Committee retained Goodwin Procter LLP ("Goodwin") to assure that the Compensation Committee was receiving independent counsel on legal aspects of the new compensation program.'
, {'entities': []})
, ('In addition, the Committee refers to market data based on manufacturing companies within the Aon Hewitt TCM Online Executive survey using regression analysis and tabular long-term incentive data and Mercer Executive Compensation survey with a revenue range of $5 billion to $20 billion for corporate executives and $1.2 billion to $1.375 billion for the operating executives.'
, {'entities': [(93,103, 'CC'), (199,205,'CC')]})
, ("In 2007, the Compensation Committee increased Mr. Roth's annual dollar credit under CAP to $350,000 and increased Mr. Roth's base salary by $30,000 as a substitute for his annual automobile and club allowances."
, {'entities': []})
, ('Before joining J.P. Morgan Investment Management, Mr. Cheh was a management and actuarial consultant at Towers Perrin in New York City (1991 to 1994).'
, {'entities': []})
, ('To assist the Committee in its review of named executive compensation, the Company\'s Human Resources Department, the Company\'s primary external compensation consultant, Compensia, Inc., (retained both by management and by the Committee) as well as Pearl, Meyer & Partners (retained solely by the Committee for assistance relative to CEO compensation), provide compensation data compiled both from executive compensation surveys (including proprietary surveys conducted by Radford Surveys + Consulting, Inc., Buck Consultants, LLC and Compensia, Inc.), and annual reports and proxy statements from companies that the Committee selects as a "peer group" of technology companies for executive compensation analysis purposes.'
, {'entities': [(169,184, 'CC'), (248,271,'CC'), (472,479,'CC'), (508,529,'CC'), (534,549,'CC')]})
, ('The Governance & Nominating Committee formally met three times.'
, {'entities': []})
, ('Ms. Lane is a director and sits on the Executive Committee of the board of directors of Willis Group Holdings, Ltd.'
, {'entities': []})
, ('Towers Watson also assists the Committee by reviewing comparative market data on compensation practices and programs based on an analysis of competitors included in a compensation study conducted by McLagan Partners, a compensation consulting firm that specializes in the financial services industry and that is owned by Aon Hewitt.'
, {'entities': [(0,13, 'CC'), (199,215,'CC')]})
, ("In addition to its oversight of the Corporation's internal audit organization, the Audit Committee is directly responsible for the appointment, compensation,       retention, oversight and termination of the Corporation's independent       auditors, Ernst & Young LLP (Ernst & Young), an independent       registered public accounting firm."
, {'entities': []})
, ('Prior to November 2014, Mr. Harris worked as an independent consultant and, from December 2010 until June 2013, he was Vice Chairman of Alliant Insurance Services, Inc. and President of its wholly-owned subsidiary, T&H Group, Inc. ("Alliant"), an insurance brokerage firm.'
, {'entities': []})
, ('Maintained compensation packages, with the assistance of our independent compensation consultant, so that each executive officer is within a competitive range of the median market value (50th percentile) of total compensation for executives in comparable positions.'
, {'entities': []})
, ("The Audit Committee has appointed Deloitte to serve as the Company's independent registered public accounting firm for fiscal 2014."
, {'entities': []})
, ('Ms. Cook served on the Compensation Committee until her resignation from the Board on July 4, 2014, and Ms. Donadio was appointed to the Compensation Committee effective January 1, 2015.'
, {'entities': []})
, ("The Committee reviews compensation for each of our executive officers with AonHewitt's and Towers Watson's published compensation surveys for companies with annual revenues between $5 billion and $10 billion and with compensation information disclosed in the proxy statements of our peer group."
, {'entities': [(75,84, 'CC'), (91,104,'CC')]})
, ("While Exequity performed the general competitive review, as requested by the Committee, Exequity did not determine or recommend any amount or form of executive or director compensation to the Committee with respect to McCormick's executive officers."
, {'entities': [(6,14, 'CC'), (88,96,'CC')]})
, ('Ms. Catalano currently serves on the boards of directors of Willis Group Holdings, where she serves on the governance and nominating committee, and U.S. Dataworks, where she serves as chair of the compensation committee.'
, {'entities': []})
, ('The Audit Committee regularly evaluated the performance and independence of Deloitte & Touche and, in addition, reviewed and     pre-approved all services provided by Deloitte &     Touche, the member firms of Deloitte Touche Tohmatsu, and their     respective affiliates (collectively, the Deloitte Entities)     during 2006.'
, {'entities': []})
, ("Upon closing of the Capital Transaction, the Company's former Human Resources Committee and the     former Corporate Governance and Nominating Committee were merged     into the Human Resources and Nominating Committee which is     comprised of Messrs. Lawry (Chair), Jaeckel and Hay."
, {'entities': []})
, (": The Committee determined, based on Mr. Almeida's (i) contributions to MA's operating income and Company EPS performance that for the purposes of determining incentive compensation exceeded MA's operating income and Company EPS growth targets by 9.9% and 1.0%, respectively, but also included missing Company operating income target by 2.3%, (ii) continued work on enhancing MA's product portfolio, meeting customer demand for analytic and insight tools, business development and positioning MA for growth, (iii) integration of WebEquity, (iv) focus on ensuring compliance with corporate policies and compliant internal audit results, (v) enhancement of product quality and service, (vi) contributions to the promotional"
, {'entities': []})
, ('The Compensation Committee has engaged BDO as its independent consultant for a number of years to assist the committee with its responsibilities as appropriate'
, {'entities': [(39,42, 'CC')]})
, ('The Compensation Committee engaged BDO Seidman as its independent compensation consultant to assist in a review of the compensation arrangements with Messrs. Isenberg and Petrello.'
, {'entities': [(35,38, 'CC')]})
, ("Appointment, compensation, retention, termination and oversight of the work of the Company's independent registered public accounting firm, Deloitte & Touche LLP, which reports directly to the Audit Committee"
, {'entities': []})
, ('As part of this process, the Committee considers, among other things, the continued independence of Ernst & Young, the depth of the firm??s and audit team??s experience, and the quality and efficiency of the services provided by Ernst & Young.'
, {'entities': []})
, ('?? means, subject to Paragraph IV(d), the Compensation & Management Development Committee of the Board.'
, {'entities': []})
, ('Accordingly, the Audit Committee has appointed E&Y to perform audit and other permissible non-audit services for the Company and its subsidiaries.'
, {'entities': []})
, ('The Compensation Committee retains Deloitte Consulting LLP ("Deloitte"), an independent compensation consulting firm, to provide advice on a variety of compensation matters as requested by the Compensation Committee.'
, {'entities': [(35,60, 'CC'), (61,69,'CC')]})
, ('During the past several years, including fiscal 2011, the Compensation Committee has retained Deloitte Consulting LLP ("Deloitte Consulting") to provide advice on a variety of compensation matters as requested by the Compensation Committee.'
, {'entities': [(94,117, 'CC'), (120,139,'CC')]})
, ("In fiscal 2012, the Compensation Committee retained the services of an external compensation consultant, Deloitte, to advise the Compensation Committee in its review of its named executive officer and non-executive director compensation practices, compensation trends, the design of the Company's incentive plans for its named executive officers, and, from time to time, the structure of individual executive employment agreements."
, {'entities': [(105,113, 'CC')]})
, ('In addition, the Executive Compensation Review Board ("review board"), whose members were Messrs. Dewhurst, Pimentel, Robo, the president of FPL and the most senior human resources officer, performed the initial review of the Company\'s (including its subsidiaries\') 2013 performance compared to the Annual Incentive Plan operating performance goals, including whether goals had been achieved, exceeded or missed, and made recommendations based on this review to the Compensation Committee for consideration and appropriate action.'
, {'entities': []})
, ("Further, in conjunction with ensuring the rotation of such firm's lead engagement partner, the Audit Committee and its Chair are directly involved with the selection of Deloitte's lead engagement partner."
, {'entities': []})
, ('On     March 18, 2009, our Compensation Committee made special     awards to certain employees involved in our Tamar and Gunflint     discoveries, including Messrs. Stover and Cook and     Ms. Cunningham.'
, {'entities': []})
, ("The Audit Committee believes that the appointment of Deloitte & Touche LLP (Deloitte) is in the best interests of the Company and its shareholders, and proposes and recommends that the shareholders ratify the Audit Committee's appointment of Deloitte as our independent auditor for 2015."
, {'entities': []})
, ("The Audit Committee also reviews the performance of Deloitte's lead audit partner, and the Audit Committee and its Chairperson oversee the rotation of Deloitte's lead audit partner and are involved in the selection of the lead audit partner."
, {'entities': []})
, ("In addition, at each regularly scheduled Audit Committee meeting, the Audit Committee conducted a private session with Office Depot's Internal Audit executive as well as Deloitte, without the presence of other management."
, {'entities': []})
, ('Based on our Chief Executive Officer and the Compensation Committee??s general knowledge of base salaries paid to similarly positioned executives at companies of comparable size and profitability, review of data provided by Cook & Co. with respect to certain executives, and the Compensation Committee??s emphasis on performance-based compensation, the base salaries for Messrs. Wren, Hewitt and O??Brien were not adjusted in 2014.'
, {'entities': []})
, ("During fiscal year 2008, Gordon A. Campbell, Fred D. Anderson, William T. Coleman and D. Scott Mercer served as members of the Compensation Committee of Palm's board of directors, none of whom is or has been an officer or employee of Palm or any of its subsidiaries."
, {'entities': []})
,("In October 2007, Hewitt Associates replaced Buck Consulting as the Committee's Compensation Consultant."
, {'entities': [(44,59, 'CC'), (17,34,'CC')]})
, ('In addition, management and the Committee periodically review compensation survey data published by Mercer Human Resource Consulting, Towers Watson, Aon Hewitt, SIRS and the Hay Group.'
   , {'entities': [(100,132, 'CC'), (134,147,'CC'), (149,159,'CC'), (161,165,'CC'), (170,183,'CC')]})
, ("He also has served on the Boards of Trustees of several not-for-profit organizations, including the Lawyers Committee for Civil Rights (promoting equal justice through rule of law), the American Bar Association's Central European and Eurasian Law Initiative (promoting independent and civil rights in Eurasia), and the Asia Foundation (promoting economic and social development in Asia)."
   , {'entities': []})
, ("Consistent with past practice, in 2006, the Committee directly engaged Schuster-Zingheim, an outside compensation consultant, to assist the Committee in its evaluation of 2007 compensation for our executive officers."
   ,  {'entities': [(71,88, 'CC')]})   
, ("The Committee’s charter gives the Committee the sole authority to retain and terminate any consulting firm used by the Committee in evaluating director and officer compensation. Consistent with past practice, in 2005 and 2006, the Committee directly engaged Schuster-Zingheim and Associates, Inc. (“Schuster-Zingheim”), an outside compensation consultant, to assist the Committee in its evaluation of compensation for our executive officers and directors."
   , {'entities': [(258,296,'CC'), (299,316,'CC')]})
, ('The members of the Audit Committee are Messrs. Gardner  (Chairman),  Risch,  Solberg  and  Watson  and Mrs.  Lawson.'
   , {'entities': []})
, ('Weyerhaeuser was added to the Forest Products Peer Group used by Towers Watson for the 2015 comparative market compensation analysis that it performed for the Compensation Committee in late 2014.'
   , {'entities': []})    
, ('The Committee receives comparative compensation data from our management, from proxy statements and other public disclosures, and through surveys and reports prepared by McLagan and Towers Perrin.'
   , {'entities': [(170,177,'CC'), (182,195,'CC')]})
, ('Reports prepared by Towers Watson that relate to executive compensation may also be shared with the Committee and McLagan, and Towers Watson may, from time to time, make presentations to the Committee.'
   , {'entities': [(114,121,'CC'), (127,140,'CC')]})
, ( 'In November 2006, Deloitte presented its assessment of our executive compensation packages to the Committee, which the Committee took into consideration in connection with its approval of awards under our short-term and long-term'
   ,  {'entities': [(18,26, 'CC')]})
, ('The Compensation Committee engages Deloitte Consulting LLP, or Deloitte, to advise the Committee on executive compensation matters.'
   , {'entities': [(35,43, 'CC')]})
, ('In 2007, the Compensation Committee retained ORC Worldwide ("ORC") to provide compensation data and make recommendations to the Compensation Committee for evaluation and review of total compensation packages for our executive officers. '
   , {'entities': [(45,58,'CC'), (61,64,'CC')]})
, ('The survey information and recommendations provided by ORC were considered by the Compensation Committee, '
   , {'entities': [(55,58, 'CC')]})
, ('During 2007,     the Compensation Committee engaged Towers Perrin LLP through     August, 2007, and thereafter engaged Deloitte Consulting.'
   , {'entities': [(52,65,'CC'), (119,138,'CC')]})
, ('Prior to approval of permissible tax services by the Audit Committee, the policy requires Deloitte to (1) describe in writing to the Audit Committee (a)'
   , {'entities': []})   
, ( 'the scope of the service, the fee structure for the engagement and any side letter or other amendment to the engagement letter or any other agreement between the Company and Deloitte relating to the service and (b) any compensation arrangement or other agreement, such as a referral agreement, a referral fee or fee-sharing arrangement, between Deloitte and any person (other than the Company) with respect to the promoting, marketing or recommending of a transaction covered by the service; and (2) discuss with the Audit Committee the potential effects of the services on the independence of Deloitte.'
   , {'entities': []})   
, ("The Compensation Committee is comprised of Messieurs Bernard W.     Reznicek, D. Kent Anderson, Patrick O'Leary, John J. Shea     and William B. Smith."
   , {'entities': []}) 
, ('For 2011, the Compensation Committee engaged a compensation consultant, ClearBridge Compensation Group, to advise it on all matters related to the compensation of our Chief Executive Officer and the other executive officers and our compensation plans. The Committee has used ClearBridge Compensation Group in establishing compensation since 2009.'
   , {'entities': [(72,102, 'CC')]})
, ('Our Chief Executive Officer, Chief Human Resources Officer, and General Counsel regularly attend and participate in meetings, as do representatives of ClearBridge Compensation Group (“ClearBridge”), the Committee’s independent compensation adviser since 2009.'
   , {'entities': [(151,181,'CC'), (184,195,'CC')]})
, ('In 2006, the Compensation Committee retained Ernst &     Young LLP (E&Y) to develop a compensation benchmarking study     for our NEOs that would provide market data for base salary,     annual incentive compensation, total cash compensation,     long-term incentive compensation and total direct compensation     (cash compensation plus long-term incentive compensation) for     each NEO position.'
   , {'entities': [(45,66,'CC'), (68,71,'CC')]})
, ('the Deloitte consultants who provided services to the Compensation Committee assured the Committee that no portion of their compensation would be based on the amount or level of tax services provided by Deloitte Tax LLP to Quanta, (iii)'
   , {'entities': [(4,12, 'CC')]})
, ('Since September 2006, the Compensation Committee has engaged Alvarez & Marsal Taxand, LLC (“Alvarez & Marsal”) as its independent compensation consultant'
   , {'entities': [(61,89,'CC'), (92,108,'CC')]})
, ('The Compensation Committee directs, and works extensively with, Alvarez & Marsal to determine how Peer Group executive officer compensation data should be quantified and valued in comparison with our compensation arrangements.'
   , {'entities': [(64,80, 'CC')]})
, ('The members of our Management Development and Compensation Committee during 2007 were Barbara M. Barrett, Vernon E. Clark, Frederic M. Poses, and William R. Spivey.'
   , {'entities': []}) 
, ('In the remote event that any decision relating to Deloitte comes before the Board, the Governance and Nominating Committee or the Management Development and Compensation Committee, Ms. Stuntz would recuse herself.'
   , {'entities': []}) 
, ('During 2007, the Committee engaged McLagan, a nationally recognized financial services industry human resource consulting firm, for advice relating to Regions’ executive compensation programs and practices. While the independent consultant reports directly to the Committee, the Committee has instructed the consultant to work together with management of Regions to obtain information and further the goals of the Committee.'
   , {'entities': [(35,42, 'CC')]})
, ('The Committee does not believe there are any conflicts of interests with McLagan, because the firm does not perform work for executive management of the Company and provides no substantial services to the Company other than executive compensation consulting and related services that it provides to the Committee.'
   , {'entities': [(73,80, 'CC')]})
, ('The Compensation Committee of the Board retains McLagan (an Aon Company), a nationally recognized financial services industry human resource consulting firm, to provide ongoing advice and information regarding the design and implementation of our executive compensation programs. Since the engagement in late 2006, Mr. Brian Dunn, President of McLagan, has served the Committee in this role. McLagan’s and Mr. Dunn’s services are almost exclusively for the Compensation Committee and are more fully described in the Compensation Discussion and Analysis.'
   , {'entities': [(48,55, 'CC')]})
, ('In 2009, in addition to the executive compensation advisory services McLagan provided to the Committee, the Company also purchased from McLagan financial services industry competitive compensation survey data for positions that are not part of the Committee’s direct oversight and engaged the firm for one compensation project relating to a review of incentive plans and compensation programs in place for a particular business unit within the Company. The fees related to these non-Compensation Committee services, including the purchase of competitive survey and market data, were approved by the Chairman of the Committee and were less than $120,000 for the year.'
   , {'entities': [(69,76,'CC'), (136,143,'CC')]})
, ('Utilize an Independent Compensation Consultant (page 63)'
   , {'entities': [(69,76,'CC'), (136,143,'CC')]})
, ('In 2010, the Committee engaged Cogent Compensation Partners (“Cogent”) for advice on all executive compensation matters. Cogent is headquartered in Houston, Texas and provides independent compensation advice to companies in the Fortune 500, focusing on the energy industry.'
   , {'entities': [(31,59,'CC'), (62,68,'CC'), (121,127,'CC')]})
, ('As in the past, the Compensation Committee continued to engage the services of Compensia, Inc., an independent, national compensation consulting firm (the “compensation consultant”) that provides the Compensation Committee and the Board of Directors with guidance regarding the amount and types of compensation that we provide to our executives, how these compare to peer company compensation practices and advice regarding other compensation-related matters. '
   , {'entities': [(79,94, 'CC')]})
, ('Maintained an engaged, independent and experienced Compensation Committee comprised of leaders with significant business and technology industry experience, which met nine times in fiscal 2015;'
   , {'entities': []}) 
, ('This limit was decided in connection with the adoption of the 2013 Plan, and after consultation with the Compensation Committee’s independent compensation consultant, Compensia, Inc.'
   , {'entities': [(167,182, 'CC')]})
, ('The individual compensation elements are intended to create a total compensation package for each Named Executive Officer that we believe achieves our compensation objectives and provides competitive compensation opportunities. From time to time, management has retained Buck Consultants, an independent compensation consulting firm, to review and identify our appropriate peer group companies, and to obtain and evaluate current executive compensation data for these companies. '
   , {'entities': [(271,287, 'CC')]})
, ('Includes pro rata fee of $1,051 which was earned by Mr. Mercer for his Compensation Committee service in the first quarter of fiscal year 2014.'
   , {'entities': []}) 
, ('Except where pre-approval is not required by Securities and Exchange Commission rules, the committee pre-approves all audit and permissible non-audit services provided by Deloitte & Touche LLP.'
   , {'entities': []}) 
, ('Since 2002, the Compensation Committee has retained     Ernst & Young, LLP, or E&Y, as its independent     compensation consultant to advise it on all matters related to     compensation of our senior management, including our principal     executive officer, the Chief Executive Office ("CEO"),     our principal financial officer, the Executive Vice President     and Chief Financial Officer ("EVP & CFO" or     "CFO"), Executive Vice President and     President-Exploration & Production'
   , {'entities': [(56,74,'CC'), (79,82,'CC')]})
, ('The Audit     Committee has established a policy requiring its pre-approval of     all audit and permissible non-audit services provided by     Deloitte.'
   , {'entities': []})
, ('The Compensation Committee has the sole authority to retain and supervise one or more outside advisors, including outside counsel and consulting firms, to advise the Committee on executive and director compensation matters and to terminate any retained adviser.'
   , {'entities': []})
, ('For executive officer positions for which there were not similar positions at peer group companies or when supplemental data is considered necessary for a fair comparison, the Committee used additional information obtained from Towers Watson and McLagan Partners or compiled by management from publicly available sources.'
   , {'entities': [(228,241,'CC'), (246,262,'CC')]})
, ('The current members of the Nominating, Governance and Compliance Committee are directors Frederic Poses, who chairs the committee, and John Van Scoter.'
   , {'entities': []})
, ('The Committee pre-approves all audit and non-audit services provided by Ernst & Young LLP to the Company and its subsidiaries and approves the overall scope and plans for their audit activities, including the adequacy of staffing and compensation.'
   , {'entities': []})
, ("Further, in conjunction with the mandated rotation of the audit firm's lead engagement partner, the Audit Committee and its Chair are involved in the selection of Deloitte's new lead engagement partner."
   , {'entities': []})
, ("For 2007, the committee's standard executive merit increase was 3.5%, although its average executive merit increase, excluding the newly hired CEO, was 6.25% due to adjustments made for internal and external pay equity."
   , {'entities': []})
, ('In 2006, the Committee directly engaged Mercer Human     Resource Consulting ("Mercer") and Korn/Ferry     Executive Compensation Advisors ("Korn Ferry")'
   , {'entities': [(40,76,'CC'), (79,85,'CC'), (92,138,'CC'), (141,151,'CC')]})
, ('Accordingly, the Audit Committee has appointed E&Y to perform audit and other permissible non-audit services for the Company and its subsidiaries.'
   , {'entities': []})
, ('In establishing bonus payments for the executive officers, the Committee consulted with representatives of Korn/Ferry Compensation Advisors, its compensation consultant'
   , {'entities': [(107,117, 'CC')]})
, ('In early 2007, the Compensation Committee retained Executive Compensation Advisors, a Korn/Ferry company (“ECA”), as its independent compensation consultant.'
   , {'entities': [(86,96, 'CC')]})
, ('During 2010, the Compensation Committee retained ClearBridge Compensation Group (“ClearBridge”) as its sole compensation advisor.'
   , {'entities': [(49,79,'CC'), (82,93,'CC')]})
, ('During 2014, the Compensation Committee retained ClearBridge Compensation Group (“ClearBridge”) as its sole compensation advisor.'
   , {'entities': [(49,79,'CC'), (82,93,'CC')]})
, ('Members of the Compensation Committee are John A. Luke, Jr. (Compensation Committee Chairman), John M. Ballbach, Diane C. Creel, Joseph W. Ralston, John P. Reilly and Jacqueline F. Woods.'
   , {'entities': []})
, ('The compensation recommendations and decisions for 2012 of our management, the Compensation Committee, with the aid of its independent compensation consultant, Board Advisory, LLC, and the independent members of the Board in the case of the persons who served as Chief Executive Officers during 2012 are summarized in the separate executive summary of Compensation Discussion and Analysis on page 25 of this Proxy Statement.'
   , {'entities': [(160,179, 'CC')]})
, ('During the past several years, including fiscal 2013, the Compensation Committee has retained Deloitte Consulting LLP ("Deloitte Consulting") to provide advice on a variety of compensation matters as requested by the Compensation Committee.'
   , {'entities': [(94,117,'CC'), (120,139,'CC')]})
, ('Accordingly, the Audit Committee has appointed E&Y to perform audit and other permissible non-audit services for the Company and its subsidiaries.'
   , {'entities': []})
, ('The members of the Management Development and Compensation Committee are directors Frederic Poses, who chairs the committee, Robert Hernandez and Daniel Phelan.'
   , {'entities': []})
, ("Finally, contrary to the shareowner proposal's claim, Michael Eskew does not serve on the Compensation Committee and qualifies as an independent director under the NYSE listing standards, although the board has determined that he is not independent for UPS's purposes."
   , {'entities': []})
, ("The Compensation Committee directly engages PricewaterhouseCoopers LLP as a compensation consultant to provide advice on executive compensation matters, and it has performed such duties in Fiscal 2007."
   , {'entities': [(44,70, 'CC')]})
, ('During Fiscal 2010, the Company also retained PricewaterhouseCoopers LLP to provide services unrelated to executive compensation including tax-related services.'
   , {'entities': [(46,72, 'CC')]})

, ('The Audit Committee has appointed E&Y as the company??s independent accountants to audit the consolidated financial statements of the company for fiscal 2015.'
   , {'entities': []})
, ('The Compensation Committee has designed and administered an executive compensation program to reward executives for the achievement of strategic and operational goals as well as increased shareholder value and to attract and retain talented leaders to guide Weatherford to its fullest potential.'
   , {'entities': []})
, ("In connection with Mr. Almeida's 2014 compensation review, the committee considered compensation information from the 2013 Towers Watson U.S. Compensation Data Bank General Industry Executive Compensation Database (which included data from 119 companies with annual revenues greater than $2 billion); 2013 Mercer Benchmark Database-Executive (which included data from 24 companies with annual revenues between $2.5 billion and $5 billion); AonHewitt 2013 US Total Compensation Measurement Database (which included data from 69 companies with annual revenues between $2.5 billion and $5 billion); and Equilar \x96 President America & Europe Compensation Survey (which included data from three companies with a median"
   , {'entities': [(123,136,'CC'), (306,312,'CC'), (440,449,'CC'), (600,607,'CC')]})
, ("going forward with WestRock, we would continue with the overall compensation policies that RockTenn's compensation committee had implemented with respect to RockTenn prior to the Combination."
   , {'entities': []})
, ('Buck Consultants, an ACS subsidiary, replaced Mercer as the consultant to management shortly after the acquisition of ACS by Xerox.'
   , {'entities': [(46,52, 'CC')]})
, ('General Partner, InterWest Partners, Chair of the Compensation Committee of the Board'
   , {'entities': []})
, ('The Committee uses the services of an outside executive compensation consultant, McLagan, to provide guidance and advice to the Committee on all matters covered by its charter.'
   , {'entities': [(81,88, 'CC')]})
, ("situated executives at peer financial institutions, based on a study prepared by the Committee's independent executive compensation consulting firm, McLagan, an Aon Hewitt Company, or McLagan."
   , {'entities': [(149,156,'CC'), (161,179,'CC')]})
, ( 'Since 1996, Mr. Neff has served as Chairman of Spencer Stuart, U.S. Mr. Neff is a director of Hewitt Associates, Inc. where he serves on the Compensation and Leadership Committee and the Governance Committee.'
   , {'entities': []})
, ('Our Compensation Committee has the authority to retain independent consultants, and, in fiscal 2006, engaged Johnson Associates, Inc. to assist it. It also evaluates the performance of the Chief Executive Officer and discusses the evaluation with all non-employee directors in executive session.'
   , {'entities': [(109,133, 'CC')]})
, ("The Committee has the authority under its charter to engage the services of outside advisors, experts and others to assist the Committee. The Committee has engaged Aon Consulting, which, together with James G. Purvis, Executive Vice President of Human Resources, and his executive compensation team, supports the Committee in its work. "
   , {'entities': [(164,178, 'CC')]})
, ('The Committee has engaged Barney & Barney LLC (“Barney & Barney”) as its independent compensation consultant.'
   , {'entities': [(26,45, 'CC'), (48,63,'CC')]})
, ("The Committee has the authority under its charter to engage the services of outside advisors, experts and others to assist the Committee. The Committee has engaged Aon Consulting (“Aon”), as its independent compensation consultant."
   , {'entities': [(164,178, 'CC'), (181,184,'CC')]})
, ("Aon provides the Committee with an independent view of both market data and plan design. Aimco management has engaged Ferguson Partners to assist in designing Aimco’s executive compensation plan. Neither Aon nor Ferguson Partners provided other services to the Company in excess of $120,000."
   , {'entities': [(0,3,'CC'), (118,135,'CC'), (204,207,'CC'), (212,229,'CC')]})
, ('he Compensation and Human Resources Committee currently consists of the seven Independent Directors. Mr. Keltner serves as the chairman of the Compensation and Human Resources Committee. Mr. Keltner meets regularly with Ms. Cohn, Aimco’s General Counsel and with Jennifer Johnson, Aimco’s Senior Vice President of Human Resources. Mr. Keltner also has regular conversations with the Committee’s independent compensation consultant, Board Advisory, LLC (“Board Advisory”). The Compensation and Human Resources Committee has a written charter that is reviewed annually and was last amended in April 2013. The Compensation and Human Resources Committee’s charter is posted on Aimco’s website (www.aimco.com) and is also available in print to stockholders, upon written request to Aimco’s Corporate Secretary.'
   , {'entities': [(432,451, 'CC'), (454,470,'CC')]})
, ('In 2006 we utilized the services of a compensation consulting company during the year. We had a contract with the Radford Group of AON Consulting Inc. for the first six months of 2006. The Radford Group provided us with their Radford Benchmark Survey, the Radford Executive Survey, the Radford Sales Survey and the Radford International Survey. All these surveys were used to ascertain the reasonableness of amounts and types of compensation paid to our employees and executives. The Radford Group was paid $14,700 for their services.'
   , {'entities': [(114,150,'CC'), (185,202,'CC'), (226,233,'CC'), (256,263,'CC'), (286,293,'CC'), (315,322,'CC'), (484,491,'CC')]})
, ("It is the goal of our compensation committee to establish salary compensation for our executive officers based on our operating performance relative to comparable software and computer peer companies over a three to five year period. In setting base salaries for fiscal 2007, we reviewed studies conducted and recommendations issued by the Radford Group of AON Consulting Inc. "
   , {'entities': [(340,347, 'CC')]})
, ("The Compensation Committee of the Board of Directors reviews and approves our overall compensation strategy and policies. The Compensation Committee reviews and approves corporate performance goals and objectives relevant to the compensation of our executive officers and other senior management; reviews and approves the compensation and other terms of employment of our Chief Executive Officer; reviews and approves the compensation and other terms of employment of the other executive officers; and administers our stock option and purchase plans, pension and profit sharing plans, stock bonus plans, deferred compensation plans and other similar programs. We also have a Non-Officer Option Committee, established in May 1997, which has the power to award stock options to non-officer employees and consultants. The Compensation Committee is presently composed of two non-employee directors: Messrs. Dixon and Lee (Chairman). All members of our Compensation Committee are independent (as independence is currently defined in Rule 4200(a)(15) of the Nasdaq listing standards). The sole member of the Non-Officer Option Committee is Dr. Chen. In 2008, the Compensation Committee met 4 times."
   , {'entities': []})
, ('Stoel Rives LLP was retained by the Savings & Retirement Plan (401k) Administrative Committee in the third quarter of 2012, in place of Mercer Human Resources Consulting, to advise this committee on plan design, compliance and operational consulting for our qualified defined contribution plan.'
   , {'entities': [(0,15,'CC') ]})
, ('The HRC has determined that the work of Towers Watson, Mercer Investment Consulting and Stoel Rives LLP did not raise any conflicts of interest in fiscal 2013. In making this assessment, the HRC considered that neither Towers Watson, Mercer Investment Consulting nor Stoel Rives LLP provided any other services to the Company unrelated to executive compensation and the other factors enumerated in Rule 10C-1(b) under the Exchange Act.'
   , {'entities': [(40,53, 'CC'), (55,83,'CC'), (88,103,'CC'),(219,232, 'CC'), (234,262,'CC'), (267,282,'CC') ]})
, ('In early 2005, a subcommittee of the Compensation Committee awarded equity incentive grants for the first year of a three-year program developed and approved by the Committee, with assistance from its consultant, PricewaterhouseCoopers LLP. Based on data compiled by PricewaterhouseCoopers, the Subcommittee determined that the target amount of long-term compensation proposed for 2005, 2006 and 2007 was consistent with its goal of granting long-term incentive awards with a value commensurate with those paid to similarly-situated executives at comparable companies. In both February 2006 and 2007, the Committee confirmed that the amount of long-term compensation targeted for 2006 and 2007 was still appropriate, and approved grants to the executive officers in such amounts. For the reasons discussed above, the Committee split these awards between stock options and restricted stock. For more information, see the tables included under the heading “Executive Compensation.” '
   , {'entities': [(213,239, 'CC'), (267,289,'CC')]})
, ('In February 2008, the Compensation Committee determined that the salary of each of its executives was generally in alignment with the 75th percentile target salary based on 2007 compensation data provided by PricewaterhouseCoopers LLP, the Committee’s compensation consultant.'
    , {'entities': [(208,234, 'CC')]})
, ("Data drawn from the restaurant peer group is adjusted by using regression analysis to eliminate variations in compensation level attributable to differences in size of the component companies. Compensation Strategies, the committee’s independent executive compensation consultant, performs this analysis. "
    , {'entities': [(193,216, 'CC')]})
, ('The committee’s outside compensation consultant, Compensation Strategies, also provides input on compensation decisions, including providing comparisons to market levels of compensation as described below under “—Market Data.”'
    , {'entities': [(49,72, 'CC')]})
, ("Our Compensation Committee, which is advised by Compensation Strategies, an independent compensation consultant that did not perform other work for Chipotle during 2013, has structured and implemented executive compensation programs that encourage long-term shareholder value creation. During 2013, we once again grew significantly and met or exceeded all of the operating and financial performance guidance we announced prior to the beginning of the year. And importantly, we achieved these results without raising menu prices, which likely would have contributed to even more robust sales and profit growth. For more detail regarding our business performance and creation of shareholder value, see “Compensation Discussion and Analysis—Overview of the Performance Based Nature of our Executive Compensation” beginning on page 42 below. Almost every significant development with respect to the compensation of our executive officers in 2013 was driven by or in recognition of this strong performance. "
    , {'entities': [(48,71, 'CC')]})
, ("The Committee's compensation consultant performs executive compensation services only at the request of the Committee and does not perform services for management. In 2008, the Committee engaged Longnecker & Associates as its compensation consultant. "
    , {'entities': [(195,218, 'CC')]})
, ('the Compensation and Governance Committee has engaged the firm of Longnecker & Associates (“Longnecker”) as its independent compensation consultant to fulfill the following responsibilities:'
   , {'entities': [(66,89, 'CC'), (92,102,'CC')]})
, ('The Committee uses Longnecker & Associates ("Longnecker"), an independent compensation consultant, for information and advice about program design and implementation and to ensure that the design and elements of compensation are consistent with the objectives of the program. Longnecker does not perform services for management. During 2011, the Committee engaged Longnecker to provide the following services'
   , {'entities': [(19,42, 'CC'), (45,55,'CC'), (364,374,'CC') ]})
, ('Since 2009, the committee has engaged Veritas Executive Compensation Consultants, LLC to serve as its independent advisor.'
    , {'entities': [(38,85, 'CC')]})
, ('In October 2009, the compensation committee retained Veritas Executive Compensation Consultants, LLC to serve as an independent advisor to the committee.' 
    , {'entities': [(53,100, 'CC')]})
, ('The Company also engages its own consultants, which have included Exequity LLC, Meridian Compensation Partners LLC and Towers Watson, to provide advice on the design of various compensation programs. Specifically in 2010, the Company used its compensation consultants to '
   , {'entities': [(66,78, 'CC'), (80,114,'CC'), (119,132,'CC') ]})
, ('Prior to selecting Veritas as its independent advisor, the committee would from time to time retain Towers Watson (formerly Towers Perrin), an outside compensation and benefits consulting firm, regarding management pay, compensation design and other related matters.'
   , {'entities': [(19,26, 'CC'), (100,113,'CC'), (124,137,'CC') ]})
, ('Executive Compensation Process and Procedures:  Over the course of several meetings throughout the year, the Compensation Committee annually reviews executive compensation, including base salary, short-term incentive compensation, long-term incentive compensation and other benefits. In performing its duties, the Compensation Committee obtains input, as it deems necessary, from Pay Governance (formerly part of Towers Watson), an independent compensation consultant (“Compensation Consultant”) engaged directly by the Compensation Committee (while the Compensation Consultant is engaged by the Compensation Committee, it works with management, including members of our human resources department and our CEO, in developing compensation studies as directed by the Compensation Committee). In addition, in the case of compensation decisions relating to executives other than the CEO, the Compensation Committee seeks and obtains input from the CEO. The Compensation Committee regularly holds executive sessions at its meetings during which management, including the CEO, is not in attendance. Additional information regarding the Compensation Committee’s processes and procedures for consideration and determination of executive compensation is provided below at “VII. Executive Compensation—Compensation Discussion and Analysis.” '
   , {'entities': [(380,394, 'CC'), (413,426,'CC')]})
, ('Consistent with past practices, in 2007 the Committee retained a compensation consultant, Gressle & McGinley, LLC (the “Compensation Consultant”), to assist the Committee in its process of identifying and establishing peer groups of companies, reviewing the compensation programs of members of the peer groups and making recommendations and providing advice with respect to compensation of the Company’s executive officers. The Compensation Consultant was also engaged to conduct a detailed review of supplemental equity programs maintained by other real estate investment trusts (“REITs”), to advise the Committee with respect to the establishment of parameters for the 2007 Supplemental Equity Program and to work with the Committee and the Company’s management to establish a program that is designed to incentivize executive officers and increase shareholder value.'
    , {'entities': [(90,113, 'CC')]})
, ('''For 2010, the Committee retained Gressle & McGinley as its independent compensation consultant. Gressle & McGinley assisted the Committee in:'''
   , {'entities': [(33,51, 'CC')]})
, ("The Committee utilized Gressle & McGinley’s experience in developing and analyzing compensation programs to help it establish all aspects of 2009 compensation for Messrs. Wolstein and Hurwitz. In connection with the company’s renegotiation of the employment agreements for Messrs. Wolstein and Hurwitz in July 2009, as described in further detail below, Gressle & McGinley provided the Committee with detailed comparative compensation data for the two most senior executive officers within the AUM sample, as described further below."
   , {'entities': [(23,41, 'CC'), (354,372,'CC')]})
, ("Gressle & McGinley also provided the Committee with benchmarking information in connection with the design and implementation of our new Value Sharing Equity Program, as described further below, and in changes to our director compensation program. In early 2010, Gressle & McGinley also facilitated the Committee’s review of our 2009 financial performance, Messrs. Wolstein and Hurwitz’s performance and the level of annual performance-based compensation that had been earned by Messrs. Wolstein and Hurwitz for 2009."
   , {'entities': [(0,18, 'CC'), (263,281,'CC')]})
, ("The Compensation Committee has engaged Sibson Consulting as a compensation consultant to work collaboratively with the Committee for the fiscal year beginning July 1, 2007."
    , {'entities': [(39,56, 'CC')]})
, ("The Compensation Committee also engaged The Delves Group as compensation consultants to review management’s recommendations and provide data and insights to ensure that our executive compensation program is fair, reasonable, and consistent with our compensation objectives. The role of The Delves Group involved in our compensation processes was purely advisory in nature and the Compensation Committee retained ultimate responsibility for its compensation-related decisions. "
   , {'entities': [(40,56, 'CC'), (286,302,'CC')]})
, ('''For fiscal year 2008, management worked with Frederic W. Cook and Co., as described below, on its long-term incentive program and with Hewitt Associates on benchmarking the total compensation of its executive team. The Compensation Committee engaged Sibson Consulting to review management’s recommendations and provide data and insights that ensure that our executive compensation program and directors’ compensation program are fair, reasonable, and consistent with our compensation objectives. The role of all of the outside consultants involved in our compensation processes was purely advisory in nature and the Compensation Committee retained ultimate responsibility for its compensation-related decisions.'''
   , {'entities': [(45,69, 'CC'), (135,152,'CC'), (250,267,'CC') ]})
, ("For fiscal year 2009, management worked with Frederic W. Cook and Co. on the design of the long-term incentive element of our compensation program and used widely-published surveys (Towers Perrin and Mercer) for input into many of the decisions related to the total compensation of its executive team. The Compensation Committee engaged The Delves Group to review management’s recommendations and provide data and insights that ensure that our executive compensation program is fair, reasonable, and consistent with our compensation objectives. The role of all of the outside consultants involved in our compensation processes was purely advisory in nature and the Compensation Committee retained ultimate responsibility for its compensation-related decisions. "
   , {'entities': [(45,69, 'CC'), (182,195,'CC'), (200,206,'CC') ]})
, ('''For fiscal year 2010, management used widely-published surveys (provided by Watson Wyatt, Towers Perrin and Mercer) to help inform many of the decisions related to the total compensation of its executive team. The Compensation Committee engaged The Delves Group to review management’s recommendations and provide data and insights that ensure that our executive compensation program is fair, reasonable, and consistent with our compensation objectives. The role of the outside consultants involved in our compensation processes was purely advisory in nature and the Compensation Committee retained ultimate responsibility for its compensation-related decisions. '''
   , {'entities': [(76,88, 'CC'), (90,103,'CC'), (108,114,'CC'), (245,261,'CC') ]})
, ('The Committee has retained an independent compensation consultant, The Croner Company (“Croner”), to advise it on compensation matters generally and specifically on compensation decisions for our executive officers. Croner is retained directly by, and reports to, the Committee.'
   , {'entities': [(67,85, 'CC'), (88,94,'CC'), (216,222,'CC') ]})
, ('In early 2013, the Committee reviewed its relationship with Croner as an independent compensation consultant and, after considering the factors set forth in the applicable securities regulations, concluded that Croner did not have a conflict of interest in its services to the Committee. The Committee conclusion was based on the following: '
   , {'entities': [(60,66, 'CC'), (211,217,'CC')]})
, ("Croner reports solely to the Committee. Discovery’s management is not involved in the negotiation of fees charged by Croner or in the determination of the scope of work performed by Croner. The Committee has the sole authority to hire and terminate the independent compensation consultant;"
   , {'entities': [(0,6, 'CC'), (117,123,'CC'), (182,188,'CC') ]})
, ('During 2014, the Committee directly engaged Lyons, Benenson & Company Inc. (Lyons Benenson), a compensation consultant, to assist the Committee in developing a peer group and to provide the Committee with executive compensation survey data for that peer group. Lyons Benenson did not provide any other services to us during 2014.'
   , {'entities': [(44,74, 'CC'), (76,90,'CC')]})
, ("During 2015, the Board approved a new compensation structure for our directors, as well as director stock ownership guidelines, based on the recommendation of Lyons Benenson, as discussed further under “Director Compensation” beginning on page 46. In addition, during 2015, the Committee approved a new officer severance policy, as well as executive officer share ownership guidelines, based on the recommendation of Lyons Benenson, as discussed further under “Severance Arrangements” beginning on page 27, and “Program Governance” on page 29, respectively."
   , {'entities': [(159,173, 'CC'), (417,431,'CC')]})
, ('PM&P was engaged by the Committee to provide counsel regarding our compensation philosophy and practices, including executive and non-employee director compensation. Regarding executive compensation, the services provided to the Committee by PM&P during 2012 included a review of the principal components of compensation (base salary, cash bonus and long-term incentives), peer group selection (both compensation and performance peers), pay for performance assessment, and short and long-term incentive plan design.'
   , {'entities': [(0,4, 'CC'), (242,246,'CC')]})
, ("During 2014, the Compensation Committee received compensation advice and data from PM&P, which has served the Compensation Committee as an independent compensation consultant since 2008."
    , {'entities': [(83,87, 'CC')]})
, ('It is the Committee’s general practice not to use a compensation consultant and none was used in reviewing and determining compensation for 2006. '
   , {'entities': []})
, ("We do not use the services of outside consultants to establish or monitor our compensation programs. "
   , {'entities': []})
, ("In furtherance of the objectives of our compensation program, our compensation committee, together with the compensation committee of old FNF, engaged Strategic Apex Group, an independent compensation consultant, to conduct an annual review of our compensation programs for our named executive officers, as well as for other key executives. Strategic Apex Group provided the committees with relevant market data and alternatives to consider when making compensation decisions for the named executive officers. "
   , {'entities': [(151,171, 'CC'), (341,361,'CC')]})
, ("With respect to the total compensation levels for our shared executives, Messrs. Foley, Stinson, and Bickett, Strategic Apex Group provided the compensation committee of old FNF with a marketplace analysis based on industry specific surveys, as well as a survey based on certain old FNF peer companies. Strategic Apex Group also provided the compensation committee of old FNF with an estimate of the total compensation to be allocated to us for the services of the shared executives based upon an estimate of the time the executives would spend providing services to us. The allocation was approved by the compensation committee of old FNF, and subsequently approved by our compensation committee. "
    , {'entities': [(110,130, 'CC')]})
, ("To support its review of our executive compensation and benefit programs for 2010, the compensation committee engaged Strategic Compensation Group, an independent compensation consultant, to conduct a marketplace review of the compensation we pay to our executive officers. The compensation committee has the sole authority to approve the independent compensation consultant’s fees and terms of engagement. Strategic Compensation Group gathered marketplace compensation data on total compensation, which consisted of annual salary, annual incentives, long-term incentives, executive benefits, executive ownership levels, overhang and dilution from the equity incentive plan, compensation levels as a percent of revenue, pay mix and other key statistics. The marketplace compensation data provided a point of reference for our compensation committee, but our compensation committee ultimately made compensation decisions based on all of the factors described above. "
   , {'entities': [(118,146, 'CC'), (407,435,'CC')]})
, ("To further the objectives of our compensation program, the compensation committee engaged Strategic Apex Group, an independent compensation consultant, to conduct an annual review of our compensation programs for the named executive officers, as well as for other key executives. Strategic Apex Group provided the compensation committee with relevant market data and alternatives to consider when making compensation decisions for our key executives, including the named executive officers. "
   , {'entities': [(90,110, 'CC'), (280,300,'CC')]})
, ("To assist the compensation committee in determining 2008 compensation levels, Strategic Compensation Group gathered marketplace compensation data on total compensation, which consisted of annual salary, annual incentives, long-term incentives and pay mix. Strategic Compensation Group used two different marketplace data sources: (i) general compensation surveys prepared by Hewitt Associates and Towers Perrin, which together contain data on approximately 700 companies; and (ii) a group of 17 publicly-traded companies. The 17 companies were: "
    , {'entities': [(78,106, 'CC'), (375,392,'CC'), (397,410,'CC') ]})
, ('Strategic Compensation Group used three marketplace data sources: (1) a general executive compensation survey prepared by Towers Watson, which contained data on over 300 companies (in using this survey, our compensation committee applied a formula contained in the survey that allows for the adjustment of the survey\'s compensation amounts to take into account differences in revenues between the survey companies and our Company), (2) a general executive compensation survey of over 3,000 companies with a specific focus on companies with revenues of between $5 billion and $9 billion and (3) compensation information for the following group of 17 companies, which we refer to as our "peer group.'
    , {'entities': [(0,28, 'CC')]})
, ('Independent Business Adviser and Consultant.'
   , {'entities': []})
, ("Historically, there has not been a pre-established policy or target for the allocation between either cash and non-cash or short and long-term incentive compensation. The CEO and Chairman review information, surveys and other information considered relevant, which may, but in 2008 did not, include information from consultants, to determine the appropriate level and mix of incentive compensation for each executive officer and make recommendations to the Compensation Committee, which also has access to the background material reviewed by the CEO and Chairman. The portion of an executive's total compensation that is contingent upon our performance tends to increase commensurate with the executive's position within our Company. This approach is designed to provide more upside potential and downside risk for those senior positions. "
   , {'entities': []})
, ( 'The Compensation Committee believes that the terms of the Hay Agreement, which are more fully described under'
   , {'entities': []})
, ('The Compensation Committee concluded that it was desirable to provide separate supplemental retirement benefits for Mr. Hay which provide a targeted final retirement benefit at normal retirement age at a higher percentage of covered pre-retirement earnings than the SERP would otherwise provide.'
   , {'entities': []})
, ('In fiscal 2013, the Compensation Committee retained ClearBridge Compensation Group (“ClearBridge”) to advise on matters related to Director and executive compensation. ClearBridge reports directly to the Compensation Committee and does not provide any other services to the Company. '
    , {'entities': [(52,82, 'CC'), (85,96,'CC'), (168,179,'CC') ]})
, ("In fiscal 2010, the Compensation Committee engaged Pay Governance LLC (“Pay Governance”) to review the compensation programs in place for the Company’s executive officers. Pay Governance was formed during 2010 by executive compensation experts formerly with Towers Watson in order to be able to provide independent executive compensation consulting services to compensation committees of public companies. The Company had not previously retained Pay Governance for any other services. Pay Governance was engaged to perform the following on behalf of the Compensation Committee: "
   , {'entities': [(51,69, 'CC'), (72,86,'CC'), (446,460,'CC'), (485,499,'CC') ]})
, ("The Compensation Committee reviewed the independence of ClearBridge under SEC rules and NYSE listing standards regarding compensation consultants and has concluded that ClearBridge’s work for the Compensation Committee is independent and does not raise any conflicts of interest."
   , {'entities': [(56,67, 'CC'), (169,180,'CC')]})
, ("ClearBridge gathers benchmark data from our peer group, which the Compensation Committee considers among other factors (e.g., individual performance and potential, job responsibilities, historical compensation levels, etc.) in assessing and determining total compensation opportunities for the NEOs. "
    , {'entities': [(0,11, 'CC')]})
, ("Neither the company nor the MDCC currently has any contractual arrangement with any executive compensation consultant who has a role in determining or recommending the amount or form of senior executive or director compensation. Periodically, the company, through its human resources function, and the MDCC have sought the views of Frederic W. Cook & Co., Inc. about market intelligence on compensation trends along with their views on specific compensation programs designed by our human resources function, with the oversight of the MDCC. In 2006 and 2007, the company engaged Hewitt Associates on a limited basis to help ensure that the 2007 Long-Term Incentive Plan, which was approved by our shareowners at the 2007 Annual Meeting, satisfied certain technical requirements. T"
   , {'entities': [(332,360, 'CC'), (579,596,'CC')]})
, ("Periodically, the MDCC and the company’s human resources function have sought the views of Frederic W. Cook & Co., Inc. about market intelligence on compensation trends, along with its views on particular compensation programs designed by our human resources function. The company’s human resources function consulted with Frederic W. Cook & Co., Inc. in 2009 to obtain its views and information on market practices relating to certain elements of executive compensation. These services were obtained under hourly fee arrangements and not pursuant to a standing engagement."
   , {'entities': [(91,119, 'CC'), (323,351,'CC')]})
, ('During 2014, management engaged Mercer (US) Inc. to provide, using its existing sources of data, market competitive compensation data for the Chief Financial Officer and Chief Operating Officer positions at companies similar to iHeartMedia.'
    , {'entities': [(32,48, 'CC')]})
, ("During 2015, MMC was retained by management to provide services unrelated to executive or director compensation, including: an equity plan overhang analysis, consulting regarding international long-term incentive practices, leasing services, as well as insurance and brokerage services. MMC’s fees during 2015 with respect to its review of Chief Financial Officer and Chief Operating Officer compensation were $10,984, and the aggregate fees for the other services provided by MMC during 2015 were approximately $1.6 million. "
    , {'entities': [(13,16, 'CC'), (287,290,'CC'), (477,480,'CC') ]})
, ('Our Compensation Committee has the authority to retain an independent compensation consultant for the purpose of reviewing and providing guidance related to the Company’s executive compensation and benefit programs. Compensation Strategies, Inc. serves as the independent advisor and consultant to the Compensation Committee, and performs no other services for the Company.'
    , {'entities': [(216,245, 'CC')]})
, ("Since 2005, the Compensation Committee has engaged the services of Professor Brian Hall of the Harvard Business School to advise the committee with respect to executive compensation philosophy, cash incentive design, the amount of cash and equity compensation awarded, and committee process"
    , {'entities': [(67,118, 'CC')]})
, ("The Compensation Committee selected Professor Hall based on his experience and independence, and he reports directly to the Compensation Committee and interacts with management at the direction of the Compensation Committee. Professor Hall attends the Compensation Committee meetings, reviews compensation data and issues with the Compensation Committee, and participates in discussions regarding executive compensation issues. Professor Hall has not performed work for Intel other than advising on the amount or form of executive compensation pursuant to his engagement by the Compensation Committee. "
   , {'entities': [(36,50, 'CC'), (428,442,'CC')]})
, ("The Compensation Committee’s independent compensation consultant for 2008 was W.T. Haigh & Company."
    , {'entities': [(78,99, 'CC')]})
, ("As discussed in more detail in this Proxy Statement under the heading Compensation Discussion & Analysis—Role of Outside Advisors and Management at page 32, the Compensation Committee directly engaged W.T. Haigh & Company as its independent expert compensation consultant to conduct a “benchmarking” survey in 2008. The Compensation Committee also directly engaged W.T. Haigh & Company for recommendations on executive and non-employee director compensation in 2008."
   , {'entities': [(201,221, 'CC'), (365,385,'CC')]})
, ('In 2009, management retained Steven Hall & Partners for advisory services in connection with executive compensation plans, including the Company’s post-employment benefits, and Buck Consultants for actuarial work, plan structure and similar services for the Company’s retirement plans.'
   , {'entities': [(29,51, 'CC'), (177,193,'CC')]})
, ("During 2006, the Compensation Committee relied on compensation information produced by Top Five Data Services, Inc. (“Top Five”), a consulting firm retained by management."
   , {'entities': [(87,115, 'CC'), (118,126,'CC')]})
, ("From the Radford survey, we considered data from companies that had revenues between $200 million and $1 billion and located throughout Northern California, which formed our peer group data."
    , {'entities': [(9,16, 'CC')]})
, ("The committee has engaged Johnson Associates, Inc. (“Johnson Associates”), an independent consulting firm, to advise it on director and executive compensation matters. "
   , {'entities': [(26,50, 'CC'), (53,71,'CC')]})
, ("Our independent compensation consultant, Johnson Associates, Inc., is retained directly by the committee and performs no other services for the company."
    , {'entities': [(41,65, 'CC')]})
, ('''Information provided by the
committee’s consultant. Johnson
Associates advises the committee
on director and executive officer
compensation by, among other
matters:'''
    , {'entities': [(52,70, 'CC')]})
, ("Independent compensation committee consultant. Our independent compensation consultant, Johnson Associates, Inc., is retained directly by the committee and performs no other services for the company. "
    , {'entities': [(88,112, 'CC')]})
, ('In accordance with this authority, the Committee, beginning in September 2006, has engaged DolmatConnell & Partners, Inc. (DolmatConnell or the Consultant), as independent outside compensation consultant to advise the Committee on matters related to CEO and other executive compensation. DolmatConnell advises the Committee and our management on executive compensation benchmarking and program design and frequently attends the Committee meetings.'
    , {'entities': [(91,121, 'CC')]})
, ('MG Management Consultants provides the Compensation Committee with comparative compensation data, primarily for positions in the Investment Bank, and also provides such data and other services to management of the Investment Bank. The Compensation Committee does not use the services of MG Management Consultants or other compensation consultants to advise on the amount or form of senior executive compensation.'
   , {'entities': [(0,25, 'CC'), (287,312,'CC')]})
, ('The Committee retained the services of leading compensation consulting firms, Pearl Meyer & Partners and DolmatConnell & Partners (collectively "Compensation Consultants"), to advise on appropriate peer group firms, pay levels and mix, incentive plan design, performance measurement, and other relevant market practices and trends.'
   , {'entities': [(78,100, 'CC'), (105,129,'CC')]})
, ('The Compensation Committee also reviews the recommendations of the Chief Executive Officer and the Vice President-Human Resources regarding adjustment to the Company’s executive compensation programs. The Compensation Committee has retained and regularly meets with its directly retained independent executive compensation consultant, Lyons, Benenson & Co., who assists the Compensation Committee in evaluating how well the Company’s compensation programs adhere to the philosophies and principles stated below under “Compensation Discussion and Analysis.”'
    , {'entities': [(335,356, 'CC')]})
, ('The compensation elements and amounts were established by the Board after review of data prepared by Lyons, Benenson & Company Inc., the O&C Committee’s independent consultant, showing competitive director compensation levels for the Company’s high performance peer group, which is discussed under “Executive Compensation.”'
    , {'entities': [(101,131, 'CC')]})
, ('''The Compensation Committee ("Committee") of Janus' Board of Directors ("Board") retains and utilizes the expertise and advice of an independent compensation consultant, Johnson & Associates, Inc. (the "Committee Consultant"), a firm which specializes in the financial services sector and provides market compensation data and trends of relevant competitors. Compensation consultants were also retained by management to assist with analyses and recommendations to the Committee on various compensation programs.'''
    , {'entities': [(169,195, 'CC')]})
, ('''In 2007 and 2008, the Committee's compensation consultants included both McLagan and Johnson Associates, Inc. (the "Committee Consultants"). T'''
   , {'entities': [(73,80, 'CC'), (85,109,'CC')]})
, ('''In 2010, the Compensation Committee's primary compensation consultant was McLagan Partners, Inc. (the "Committee Consultant"). The Committee Consultant, which was engaged directly by the Compensation Committee, provided the Compensation Committee with market compensation data and pay trend information primarily within the financial services industry, and assisted the Compensation.'''
    , {'entities': [(74,96, 'CC')]})
, ('The     Committee has also retained The Delves Group as its independent     executive compensation consultant.'
    , {'entities': [(36,52, 'CC')]})
, ('Currently, our compensation is determined without the use of compensation consultants. Instead, we keep abreast of current trends, developments and emerging issues in executive compensation and annually compare our executive compensation components with market information, consisting of third-party surveys in which we participate. The surveys we use in reviewing our executive compensation consist of the Towers Watson Executive Survey and the Aon Hewitt Executive Survey. Over 400 companies participate in each survey. The purpose of this comparison is to ensure that our total compensation package operates effectively, remains both reasonable and competitive within the energy '
   , {'entities': [(407,420, 'CC'), (446,456,'CC')]})
, ("Our compensation is determined independently without the use of any compensation consultants.  Nevertheless, we annually compare our executive compensation components with market information, consisting of third-party surveys in which we participate.  The surveys we use in reviewing our executive compensation consist of the following: (i) Towers Watson Executive Survey, in which over 400 companies participate and (ii) the Aon Hewitt Executive Survey, in which approximately 300 to 400 companies participate."
   , {'entities': [(341,354, 'CC'), (426,436,'CC')]})
, ("For fiscal 2007, the Committee retained McLagan Partners, Inc., a firm that specializes in the financial services sector and provides market compensation data and trends of relevant competitors. As directed by the Committee, McLagan provides advice with respect to annual base salaries and incentive compensation awards for our named executive officers. McLagan also assists the Committee by providing comparative market data on compensation practices and programs based on an analysis of competitors and provides guidance on industry trends and best practices. In assisting the Committee, McLagan has assembled a list of relevant public and private competitor firms to use in comparing compensation programs. McLagan maintains the confidentiality "
    , {'entities': [(40,62, 'CC'), (225,232,'CC'), (354,361,'CC'), (590,597,'CC'), (710,717,'CC') ]})
, ("In accordance with this authority, the Committee, beginning in September 2006, has engaged DolmatConnell & Partners, Inc. (DolmatConnell or the Consultant), as its independent outside compensation consultant to advise the Committee on matters related to CEO and other executive compensation. DolmatConnell advises the Committee and our management on executive compensation benchmarking and program design and frequently attends the Committee meetings. "
    , {'entities': [(91,121, 'CC')]})
, ('The Compensation Committee directly employs its own independent compensation consultant, Compensation Strategies, Inc., and independent legal counsel, Gunderson Dettmer Stough Villeneuve Franklin & Hachigian, LLP. '
    , {'entities': [(89,118, 'CC')]})
, ('participating with management in the preparation of the Compensation Discussion and Analysis for the Company’s proxy statement; and, performing such other activities required by applicable law, rules or regulations, and consistent with its charter, as the Compensation Committee or the Board deems necessary or appropriate. The Compensation Committee may delegate to the CEO the authority to grant options to employees other than directors or executive officers, provided that such grants are within the limits established by Delaware General Corporate Law and by resolution of the Board. The Compensation Committee determines the structure and amount of all executive officer compensation, including awards of equity, based upon the initial recommendation of management and in consultation with the Compensation Committee’s outside compensation consultant. The Compensation Committee has engaged Compensation Strategies, Inc., an independent executive and director compensation consulting firm, to provide executive compensation consulting services to the Company. Additional information on the Compensation Committee’s process and procedures for consideration of executive compensation are addressed in the Compensation Discussion and Analysis below. The Compensation Committee met five times during FY 2007.'
    , {'entities': [(897,926, 'CC')]})
, ('The Compensation Committee designs our executive compensation program to be competitive with those of other companies in the semiconductor or related industries that are most similar to us in number of employees, revenue and capitalization.  The Compensation Committee determines appropriate levels of compensation for each executive officer and makes allocations between long-term and short-term as well as cash and non-cash elements of compensation.  Microchip’s financial and business objectives, the salaries of executive officers in similar positions with comparable sized companies in the semiconductor industry and individual performance may be considered in making these determinations.  If compensation information is reviewed for other companies, it is obtained from published materials such as proxy statements, and information gathered from such companies directly.  We do not engage consultants to conduct such review process for us.'
   , {'entities': []})
, ("The Compensation Committee designs our executive compensation program to be competitive with those of other companies in the semiconductor or related industries that are similar to us in terms of number of employees, revenue and capitalization. The Compensation Committee determines appropriate levels of compensation for each executive officer based on their level of responsibility within the organization, performance, and overall contribution. After such determination, the Compensation Committee makes allocations between long-term and short-term as well as the cash and non-cash elements of compensation. Microchip's financial and business objectives, the salaries of executive officers in similar positions with comparable companies and individual performance are considered in making these determinations. If compensation information is reviewed for other companies, it is obtained from published materials such as proxy statements, and information gathered from such companies directly. We do not engage consultants to conduct such review process for us or utilize a specific peer group."
   , {'entities': []})
, ('We obtain information on the compensation levels, programs and practices of the companies within the peer group annually from market surveys conducted by Wachovia Insurance Services National Compensation Consulting Firm, a compensation consultant engaged by the Committee.  The Committee evaluates compensation levels for our named executive officers based upon a comparison to the market median values. The above peer group is the one we used for targeting and evaluating the compensation levels of our named executive officers for 2006. As our strategy changes and we leverage our capabilities into other markets, we will review the peer group, annually, to assure that it has an appropriate basis of comparison. '
    , {'entities': [(154,219, 'CC')]})
, ('The Compensation and Human Resources Committee engages Compensation Strategies, Inc. (Compensation Strategies) as its compensation consultant to provide independent advice and assist in the development and evaluation of the Company executive and director compensation policies. The role of Compensation Strategies with respect to compensation decisions in 2006 is set forth in more detail in the Compensation Discussion & Analysis beginning on page 28.'
   , {'entities': [(55,84, 'CC'), (86,109,'CC')]})
, ('The HRNC engaged LB&Co. for 2015 as MoneyGram’s independent compensation consultant to assist and advise the HRNC on all aspects of the Company’s executive and director compensation programs and corporate governance. LB&Co. attended or participated by teleconference in all meetings of the HRNC in 2015.'
   , {'entities': [(17,22, 'CC'), (217,222,'CC')]})
, ('In determining the compensation of our NEOs for 2011, the Compensation Committee took into account the realities of the current economic environment and the goals that the Company desired to achieve in such environment (as described above). The Compensation Committee also took into account the Company’s near-term financial results, the many contributions of our NEOs that are not fully reflected in our near-term financial results, the highly competitive nature of the Company’s industry, compensation data about the Company’s peer group provided by the Compensation Committee’s independent compensation consultant (Buck Consultants, LLC) and the need to attract, retain and motivate a team of highly qualified and dedicated senior executives who are critical to the long-term success of the Company. '
    , {'entities': [(618,639, 'CC')]})
, ('Management regularly reaches out to significant stockholders to discuss their concerns and interests and to gather feedback, including any concerns and feedback they may have about our executive compensation practices. Our independent directors make themselves available to engage with significant stockholders as part of the Company’s ongoing stockholder outreach efforts. Additionally, the Compensation Committee obtains feedback, advice and recommendations on compensation best practices from its independent external compensation consultant, Buck Consultants, LLC (“Buck Consultants”).'
   , {'entities': [(546,567, 'CC'), (570,587,'CC')]})
, ('o assist in the development of targeted compensation levels, the Committee has retained a compensation consultant, Johnson & Associates, which specializes in working with financial services companies. The consultant reports directly and exclusively to the Committee and provides analysis and recommendations with regard to design, amount and terms of cash, equity and benefits for executive and director compensation at Moody’s. It also provides analysis regarding external benchmarking and general trends in financial services compensation. Initially, the consultant assists the Committee in identifying a group of relevant peer companies based on a review of financial services companies that are active in credit risk analysis, company and industry credit research, business information services, and other similar services for the investment community. Companies are then selected for the peer group based on common metrics which include revenue, number of employees and market capitalization.'
    , {'entities': [(115,135, 'CC')]})
, ('The Committee is empowered to retain, at the Company’s expense, such consultants, counsel or other outside advisors as it determines appropriate to assist it in the performance of its functions. In 2007, to assist in the development of targeted compensation levels, the Committee retained a compensation consultant, Johnson & Associates, which specializes in working with financial services companies. The consultant reported directly and exclusively to the Committee and provided analysis and recommendations with regard to design, amount and terms of cash, equity and benefits for executive and director compensation at Moody’s. It also provided analysis regarding external benchmarking and general trends in financial services compensation. This consultant performed no other work for the Company. For 2008, the Committee retained Hewitt Associates to act as its compensation consultant and provide services generally similar in nature to those provided by the former consultant.'
   , {'entities': [(316,336, 'CC'), (834,851,'CC')]})
, ('Executive compensation should be competitive with companies within our peer group and also recognize individual performance.  In order to attract and retain experienced executive officers, our total compensation packages need to be in line with what would be offered by companies within our peer group. To that end, we have retained Hewitt Associates, a nationally recognized independent compensation consulting firm, which provides us with peer comparables and other information, as well as views and advice on compensation-related matters. We also analyze overall compensation very carefully to ensure we are recognizing subjective factors such as responsibilities, position and individual performance including but not limited to such qualities as leadership, strategic vision and execution of corporate initiatives. We are also cognizant that as we continue to pursue our strategic initiatives and growth strategies, the companies constituting our peer group will change, and we have therefore reviewed and adjusted our total executive compensation packages accordingly and will continue to review them in the future. Our Compensation Committee has direct access to Hewitt regarding any issues that arise within the Compensation Committee’s authority, and while the Compensation Committee also seeks and receives input from management on executive compensation issues (for example, on the criteria and specific target levels for awards under our short-term and long-term performance-based incentive plans), decisions on these matters are made solely by our Compensation Committee.'
   , {'entities': [(333,350, 'CC'), (1170,1176,'CC')]})
, ('The Compensation Committee engaged BDO Seidman as its independent compensation consultant to assist in a review of the compensation arrangements with Messrs.'
    , {'entities': [(35,46, 'CC')]})
, ("Role of Compensation Consultants. In 2011, Occidental participated in compensation surveys conducted by Towers Watson, Frederic W. Cook & Co. and other compensation consultants in order to better understand general external compensation practices, including executive compensation. From time to time, Occidental, through its executive compensation department or the Compensation Committee, will engage a consultant to provide advice on specific compensation issues. The Board’s policy on retention of independent compensation consultants adopted in 2008 is set forth in Occidental’s corporate governance policies at www.oxy.com."
   , {'entities': [(104,117, 'CC'), (119,141,'CC')]})
, ('The compensation surveys that we reviewed and summarized in the aggregate for the Committee in connection with establishing compensation for 2009 were published by: Carlson Dettmann Associates, Compensation Resources, Conference Board, Hewitt Associates, MACA, Mercer, Stanton Group (a division of Gallagher Benefits Services), Watson Wyatt Data Services and WorldAtWork.'
   , {'entities': [(165,192, 'CC'), (194,216,'CC'), (218,234, 'CC'),(236,253, 'CC'),(255,259, 'CC'),(261,267, 'CC'),(269,282, 'CC'),(298,325, 'CC'),(328,340, 'CC'),(359,370, 'CC')]})
, ("During fiscal year 2008, Gordon A. Campbell, Fred D. Anderson, William T. Coleman and D. Scott Mercer served as members of the Compensation Committee of Palm's board of directors, none of whom is or has been an officer or employee of Palm or any of its subsidiaries."
   , {'entities': []})
, ('In addition, management and the Committee periodically review compensation survey data published by Mercer Human Resource Consulting, Towers Watson, Aon Hewitt, SIRS and the Hay Group.'
 , {'entities': [(100,132, 'CC'), (134,147,'CC'), (149,159, 'CC'),(161,165, 'CC'),(170,183, 'CC')]})
, ('For 2009, the secondary general industry comparator group was based on Hewitt’s proprietary executive compensation database. The group included 84 companies with annual revenues between $8 billion and $20 billion (with median revenues of $12.3 billion and median market capitalization of $16.6 billion). A list of these 84 companies is included in Appendix B to this Joint Proxy Statement. '
    , {'entities': [(71,77, 'CC')]})
, ('In addition, supplemental data for the broader energy services segment, adjusted for PG&E Corporation’s revenues, was provided by Towers Watson from its proprietary Energy Services executive compensation survey, which includes information from over 100 energy services companies. Due to the proprietary nature of their data, Towers Watson did not disclose the companies matching individual benchmark positions.'
    , {'entities': [(130,143, 'CC')]})
, ('For 2009, the Compensation Committee engaged a compensation consultant, Executive Compensation Advisors, an affiliate of Korn/Ferry International, for a portion of the year and ClearBridge Compensation Group for the remainder of the year, to advise it on all matters related to the compensation of our Chief Executive Officer and the other executive officers and our compensation plans. The Committee used Executive Compensation Advisors in establishing compensation from 2007 into 2009'
   , {'entities': [(72,103, 'CC'), (121,145,'CC'), (177,207,'CC')]})
, ('However, in making their decision to retain Cook & Co. as the independent consultant to the Committee, the Committee noted that the financial services industry is unique in many ways and as a firm that focuses exclusively on the financial services industry, McLagan has the unique ability to provide specific market and competitive data related to compensation levels and practices in the industry.'
   , {'entities': [(44,54, 'CC'), (258,265,'CC')]})
, ('At Zep, Inc., Mr. Hall serves on the Compensation Committee and the Nominating and Corporate Governance Committee.'
   , {'entities': []})
, ('With the approval of the Chairman of the Compensation Committee, the Company retained Longnecker and Associates in 2004 to provide guidance to the Compensation Committee in connection with the Company’s employment contracts with the Chief Executive Officer, Chairman of the Board, and President of the Company.'
    , {'entities': [(86,111, 'CC')]})
, ('Longnecker and Associates was retained due to its longstanding history with the Company and its resulting understanding of the Company’s compensation practices and philosophies, in particular with respect to the Company’s employment contracts. From time to time, the Company, through its human resources department, also retains other consultants in connection with the design of compensation plans and programs that may impact executive officer compensation. As part of the review of the Company’s compensation practices discussed below under “Compensation Discussion and Analysis,” the Company requested input from Mercer Human Resource Consulting, ISS Corporate Services, Inc., and Georgeson Inc. '
   , {'entities': [(0,25, 'CC'), (617,649,'CC')]})
, ('the HC&CC engaged both Deloitte Consulting LLP and Frederic W. Cook & Co., Inc. Since the spin-off, the HC&CC has engaged Frederic W. Cook & Co., Inc. exclusively to advise it on matters related to executive compensation.'
   , {'entities': [(23,46, 'CC'), (51,79,'CC'), (122,150,'CC')]})
, ('''Executive Officer and Director Compensation Process.    Our Executive Compensation Committee has established an annual process for reviewing and establishing executive compensation levels. An outside consultant retained by the Committee has provided the Committee with relevant market data and alternatives to consider in determining appropriate compensation levels for each of our executive officers. Longnecker & Associates served as the Committee's outside consultant in 2010. Our CEO also assists the Committee in the executive compensation process. For a more thorough discussion of the roles, responsibilities and process we use for setting executive compensation, see "Compensation Discussion and Analysis."'''
    , {'entities': [(402,425, 'CC')]})
, ("As set forth in its charter, which can be found on our website, the Committee has the authority to retain and terminate compensation consultants to provide advice to the Committee. The Committee retained Longnecker & Associates in 2013 to provide information, analyses and advice regarding executive compensation. The NYSE has adopted guidelines for Compensation Committees to consider when identifying Committee advisor independence. "
    , {'entities': [(204,227, 'CC')]})
, ("These long term incentive grants were made after thorough analysis of peer group compensation (and with the assistance of Strategic Apex, an independent compensation consultant) with the goal of retaining and rewarding the Company’s most senior and valuable management. "
    , {'entities': [(122,136, 'CC')]})
   
 ]


                 
        

