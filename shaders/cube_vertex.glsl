#version 330

layout(location = 0) in vec3 in_Pos;
layout(location = 1) in vec3 in_Normal;

out vec3 pass_SurfaceNormal;
out vec3 pass_ToCameraVector;
out vec3 pass_ToLightVector;

uniform vec3 u_LightPosition;

uniform mat4 u_TransformationMatrix;
uniform mat4 u_ProjectionMatrix;
uniform mat4 u_ViewMatrix;

void main(void)
{
    vec4 worldPosition = u_TransformationMatrix * vec4(in_Pos, 1.0);
    gl_Position = u_ProjectionMatrix * u_ViewMatrix * worldPosition;

    pass_SurfaceNormal = (u_TransformationMatrix * vec4(in_Normal, 0.0)).xyz;
    pass_ToLightVector = u_LightPosition - worldPosition.xyz;
    pass_ToCameraVector = (inverse(u_ViewMatrix) * vec4(0.0, 0.0, 0.0, 1.0)).xyz - worldPosition.xyz;
}