def crop_econ_another(water, area, annual_yield, price):
    total_water = water * area
    total_yield = area * annual_yield
    total_earning = area * annual_yield * price
    ypw = total_yield / total_water
    epw = total_earning / total_water
    epa = total_earning / area
    return total_water, total_yield, total_earning, ypw, epw, epa

if __name__ == '__main__':
    crop_name_another = input('Crop:')
    water_usage_another = float(input('Estimated annual water consumption (L/rai):'))
    growing_area_another = float(input('Nation-wide growing area (rai):'))
    ypa_another = float(input('Average crop yield per growing area (kg/rai):'))
    wholesale_price_another = float(input('Estimated wholesale price (baht/kg):'))

    W_another, Y_another, E_another, YPW_another, EPW_another, EPA_another = crop_econ_another(
        water_usage_another, growing_area_another, ypa_another, wholesale_price_another
    )

    print()
    print(crop_name_another.upper(), 'over {:,.0f} rai'.format(growing_area_another))
    print('Total water usage: {:,.2f} ML'.format(W_another / 1e6))
    print('Total crop yield: {:,.2f} kg or {:,.2f} ton'.format(Y_another, Y_another / 1000))
    print('Total earning: {:,.2f} mil. baht'.format(E_another / 1e6))
    print('Average crop yield per water usage: {:,.6f} kg/L'.format(YPW_another))
    print('Average earning per water usage: {:,.6f} baht/L'.format(EPW_another))
    print('Average earning per area: {:,.2f} baht/rai'.format(EPA_another))
