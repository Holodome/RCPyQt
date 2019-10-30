#version 330

in vec3 pass_SurfaceNormal;
in vec3 pass_ToCameraVector;
in vec3 pass_ToLightVector;

out vec4 out_Color;

uniform vec3 u_LightColor;
uniform vec3 u_FaceColor;

uniform float u_Reflectivity;

void main(void)
{
    if (u_FaceColor == vec3(0.0)) discard;

    vec3 unitNormal = normalize(pass_SurfaceNormal);
    vec3 unitLightVector = normalize(pass_ToLightVector);

    vec3 unitVectorToCamera = normalize(pass_ToCameraVector);
    vec3 lightDirection = -unitLightVector;
    vec3 reflectedLightDirection = reflect(lightDirection, unitNormal);

    float specularFactor = dot(reflectedLightDirection, unitVectorToCamera);
    specularFactor = max(specularFactor, 1.0);
    float dampedFactor = pow(specularFactor, 10);

    vec3 finalSpecular = dampedFactor * u_Reflectivity * u_LightColor;

    out_Color = vec4(u_FaceColor, 1.0) + vec4(finalSpecular, 1.0);
    //    out_Color = vec4(finalSpecular, 1.0);
}