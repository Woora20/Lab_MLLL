obstructive = input('Is CAD obstructive (yes/no)? ')

if obstructive.lower() == 'no':
    print('Non-obstructive CAD.')
    print('TAVI alone.')
elif obstructive.lower() == 'yes':
    print('Obstructive CAD.')
    
    risk_area = input('Is area of myocardium at risk large (yes/no)? ')
    
    if risk_area.lower() == 'no':
        print('Small area of myocardium at risk.')
        print('Consider TAVI first, then ischemia-driven revascularization.')
    elif risk_area.lower() == 'yes':
        print('Large area of myocardium at risk.')
        
        CS = float(input('How is coronary stenosis (%)? '))
        
        if CS > 75:
            print('Severe CAD.')
            print('Staged upfront or concomitant PCI and TAVI.')
        elif CS <= 75:
            print('Moderate CAD.')
            print('Consider TAVI first, then CAD functional assessment.')
        else:
            print('CAD functional assessment needed.')

else:
    print('Invalid input. Please enter either "yes" or "no" for CAD obstructive status.')



